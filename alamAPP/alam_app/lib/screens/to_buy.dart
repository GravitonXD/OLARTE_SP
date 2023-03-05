import 'package:flutter/material.dart';
import 'package:alam_app/standards/font_styles.dart';
import 'package:alam_app/utils/stock_to_buy.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:syncfusion_flutter_charts/charts.dart';
import 'package:lottie/lottie.dart';

class BuyScreen extends StatefulWidget {
  @override
  _BuyScreenState createState() => _BuyScreenState();
}

class _BuyScreenState extends State<BuyScreen> {
  // Search Bar Controller
  final searchController = TextEditingController();
  String searchText = "";

  // Return an alert dialog
  Widget _alertDialog(String title, String content) {
    return AlertDialog(
      title: Text(title),
      content: Text(content),
      actions: [
        TextButton(
          onPressed: () {
            Navigator.of(context).pop();
          },
          child: const Text('OK'),
        ),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    Future<List<Stocks>> stocksToBuy() async {
      var url = 'https://alam.ap.loclx.io/stocks_to_buy/all';
      var response = await http.get(Uri.parse(url));
      var data = jsonDecode(response.body);
      List<Stocks> stocksToBuy = [];
      if (data['Stocks'] != null) {
        data['Stocks'].forEach((v) {
          stocksToBuy.add(new Stocks.fromJson(v));
        });
      }
      return stocksToBuy;
    }

    return Scaffold(
      appBar: null,
      body: Container(
        padding: const EdgeInsets.fromLTRB(25, 50, 25, 25),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Row(
              // To Buy Title
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Transform.translate(
                  offset: const Offset(-25, 0),
                  child: ClipRRect(
                    borderRadius: const BorderRadius.only(
                      topRight: Radius.circular(20),
                      bottomRight: Radius.circular(20),
                    ),
                    child: SizedBox(
                      width: MediaQuery.of(context).size.width * 0.4,
                      height: 45,
                      child: ColoredBox(
                        color: const Color.fromARGB(255, 66, 165, 245),
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                          children: [
                            Text(
                              "Stocks to Buy",
                              style: StandardFontStyle.headingWhite,
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),
                ),

                // Search Bar
                SizedBox(
                  width: MediaQuery.of(context).size.width * 0.45,
                  child: TextField(
                    controller: searchController,
                    keyboardType: TextInputType.text,
                    decoration: InputDecoration(
                      labelText: 'Search Stock',
                      prefixIcon: const Icon(Icons.search_outlined),
                      suffixIcon: searchController.text.isEmpty
                          ? null
                          : IconButton(
                              icon: const Icon(Icons.clear),
                              onPressed: () {
                                setState(
                                  () {
                                    // Clear input text field
                                    searchController.clear();
                                    searchText = "";
                                  },
                                );
                              },
                            ),
                      labelStyle: StandardFontStyle.bodyBlack,
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(10),
                      ),
                    ),
                    onSubmitted: (value) {
                      setState(
                        () {
                          // Search Bar
                          searchText = value;
                        },
                      );
                    },
                  ),
                ),
              ],
            ),

            // List of Stocks to Buy
            SizedBox(
              height: MediaQuery.of(context).size.height * 0.75,
              child: FutureBuilder<List<Stocks>>(
                future: stocksToBuy(),
                builder: (BuildContext context,
                    AsyncSnapshot<List<Stocks>> snapshot) {
                  try {
                    if (snapshot.connectionState == ConnectionState.done &&
                        snapshot.hasData &&
                        snapshot.data!.isNotEmpty) {
                      return ListView.builder(
                        itemCount: snapshot.data!.length,
                        itemBuilder: (BuildContext context, int index) {
                          if (searchText.isEmpty) {
                            var stock = snapshot.data![index];
                            return Card(
                              child: ListTile(
                                onTap: () {
                                  showDialog(
                                      context: context,
                                      builder: (context) {
                                        List<String> getDates() {
                                          List<String> dates = [];
                                          var date =
                                              DateTime.parse(stock.lastDate!);
                                          // Add the number of days to the current date (excluding weekends)
                                          while (dates.length <= 6) {
                                            if (date.weekday != 6 &&
                                                date.weekday != 7) {
                                              // Reformat date to show month and day only
                                              dates.add(
                                                  '${date.month}/${date.day}');
                                            }
                                            date = date
                                                .add(const Duration(days: 1));
                                          }
                                          return dates;
                                        }

                                        List<String> dates = getDates();

                                        double getMin(List values) {
                                          double min = values[0];
                                          for (int i = 0;
                                              i < values.length;
                                              i++) {
                                            if (values[i] < min) {
                                              min = values[i];
                                            }
                                          }
                                          return min - (min * 0.01);
                                        }

                                        double getMax(List values) {
                                          double max = values[0];
                                          for (int i = 0;
                                              i < values.length;
                                              i++) {
                                            if (values[i] > max) {
                                              max = values[i];
                                            }
                                          }
                                          return max + (max * 0.01);
                                        }

                                        return AlertDialog(
                                          title: Row(
                                            children: [
                                              // Icon (up arrow)
                                              const Icon(
                                                Icons.arrow_circle_up,
                                                color: Colors.green,
                                                size: 32,
                                              ),
                                              const VerticalDivider(
                                                color: Colors.black,
                                                width: 5,
                                              ),
                                              // Stock Symbol
                                              Text(stock.stockSymbol!,
                                                  style: StandardFontStyle
                                                      .titleBlack),
                                            ],
                                          ),
                                          // Chart
                                          content: SizedBox(
                                            width: MediaQuery.of(context)
                                                    .size
                                                    .width *
                                                0.8,
                                            height: MediaQuery.of(context)
                                                    .size
                                                    .height *
                                                0.2,
                                            child: SfCartesianChart(
                                              primaryXAxis: CategoryAxis(
                                                majorGridLines:
                                                    const MajorGridLines(
                                                        width: 0),
                                              ),
                                              primaryYAxis: NumericAxis(
                                                minimum: getMin(stock
                                                    .predictedClosing!
                                                    .dmdLstm!),
                                                maximum: getMax(stock
                                                    .predictedClosing!
                                                    .dmdLstm!),
                                                majorGridLines:
                                                    const MajorGridLines(
                                                        width: 0),
                                              ),
                                              plotAreaBackgroundColor:
                                                  const Color.fromARGB(
                                                      255, 227, 242, 253),
                                              tooltipBehavior: TooltipBehavior(
                                                  animationDuration: 5,
                                                  enable: true,
                                                  header: 'Date: Price (PHP)',
                                                  color: const Color.fromARGB(
                                                      255, 66, 165, 245)),
                                              title: ChartTitle(
                                                  text:
                                                      'Predicted Closing Prices for ${stock.stockSymbol!} in the next 5 Days',
                                                  textStyle: StandardFontStyle
                                                      .chartTitle),
                                              series: <
                                                  LineSeries<StockData,
                                                      String>>[
                                                LineSeries<StockData, String>(
                                                  dataSource: <StockData>[
                                                    StockData(dates[0],
                                                        stock.lastClosing!),
                                                    StockData(
                                                        dates[1],
                                                        stock.predictedClosing!
                                                            .dmdLstm![0]),
                                                    StockData(
                                                        dates[2],
                                                        stock.predictedClosing!
                                                            .dmdLstm![1]),
                                                    StockData(
                                                        dates[3],
                                                        stock.predictedClosing!
                                                            .dmdLstm![2]),
                                                    StockData(
                                                        dates[4],
                                                        stock.predictedClosing!
                                                            .dmdLstm![3]),
                                                    StockData(
                                                        dates[5],
                                                        stock.predictedClosing!
                                                            .dmdLstm![4]),
                                                  ],
                                                  xValueMapper:
                                                      (StockData x, _) => x.day,
                                                  yValueMapper:
                                                      (StockData y, _) =>
                                                          y.predictedClosing,
                                                  markerSettings:
                                                      const MarkerSettings(
                                                    isVisible: true,
                                                    color: Color.fromARGB(
                                                        255, 66, 165, 245),
                                                  ),
                                                  color: Colors.blue,
                                                ),
                                              ],
                                            ),
                                          ),
                                          actions: [
                                            // Add to Watchlist Button
                                            IconButton(
                                                onPressed: () {},
                                                icon: const Icon(Icons.work)),
                                            // Okay Button
                                            ElevatedButton(
                                              style: ElevatedButton.styleFrom(
                                                backgroundColor:
                                                    const Color.fromARGB(
                                                        255, 129, 199, 132),
                                              ),
                                              onPressed: () {
                                                Navigator.pop(context);
                                              },
                                              child: SizedBox(
                                                height: 20,
                                                width: 100,
                                                child: Center(
                                                  child: Text('DONE',
                                                      style: StandardFontStyle
                                                          .bodyWhite),
                                                ),
                                              ),
                                            ),
                                          ],
                                          actionsAlignment:
                                              MainAxisAlignment.spaceBetween,
                                          actionsPadding:
                                              const EdgeInsets.all(20.0),
                                        );
                                      });
                                },
                                visualDensity: VisualDensity.compact,
                                contentPadding: const EdgeInsets.all(15.0),
                                title: Column(
                                  mainAxisAlignment:
                                      MainAxisAlignment.spaceAround,
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text(stock.stockSymbol!,
                                        style: StandardFontStyle.headingBlack),
                                    Text('${stock.lastClosing}',
                                        style: StandardFontStyle.captionBlack),
                                  ],
                                ),
                                trailing: Column(
                                  mainAxisAlignment:
                                      MainAxisAlignment.spaceAround,
                                  crossAxisAlignment: CrossAxisAlignment.end,
                                  children: [
                                    Text(
                                      '${stock.predictedClosing?.dmdLstm?.last.toStringAsFixed(2)}',
                                      style: StandardFontStyle.headingGreen,
                                    ),
                                    Text('in 5 trading days',
                                        style: StandardFontStyle.captionBlack),
                                  ],
                                ),
                              ),
                            );
                          }
                        },
                      );
                    } else if (snapshot.connectionState ==
                            ConnectionState.done &&
                        snapshot.data!.isEmpty &&
                        searchText.isEmpty) {
                      return Center(
                        child: Text(
                          "No stocks to buy",
                          style: StandardFontStyle.captionBlack,
                        ),
                      );
                    } else {
                      return Center(
                        child: Lottie.asset('lib/assets/fetch.json'),
                      );
                    }
                  } catch (e) {
                    return Center(
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Lottie.asset('lib/assets/hasError.json'),
                          // Try Again Button
                          ElevatedButton(
                            style: ElevatedButton.styleFrom(
                              backgroundColor:
                                  const Color.fromARGB(255, 129, 199, 132),
                            ),
                            onPressed: () {
                              setState(() {});
                            },
                            child: SizedBox(
                              height: 20,
                              width: 100,
                              child: Center(
                                child: Text('Try Again',
                                    style: StandardFontStyle.bodyWhite),
                              ),
                            ),
                          ),
                        ],
                      ),
                    );
                  }
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class StockData {
  StockData(this.day, this.predictedClosing);
  final String day;
  final double predictedClosing;
}
