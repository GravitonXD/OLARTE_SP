import 'package:flutter/material.dart';
import 'package:alam_app/standards/font_styles.dart';
import 'package:alam_app/utils/file_provider.dart';
import 'dart:convert';
import 'package:http/http.dart';

class BuyScreen extends StatefulWidget {
  ServerAddressProvider serverAddressProvider;

  BuyScreen({super.key, required this.serverAddressProvider});

  @override
  // ignore: library_private_types_in_public_api
  _BuyScreenState createState() => _BuyScreenState();
}

class _BuyScreenState extends State<BuyScreen> {
  // Search Bar Controller
  final searchController = TextEditingController();
  String searchText = "";

  // Server Address
  String _serverAddress = '';

  @override
  void initState() {
    super.initState();
    widget.serverAddressProvider = ServerAddressProvider();
    widget.serverAddressProvider.readServerAddress().then((value) {
      setState(() {
        _serverAddress = value;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    var url = 'http://$_serverAddress:8000/stocks_to_buy/all';

    // function to get the data
    Future getData() async {
      // get the data
      var response = await get(Uri.parse(url));

      // decode the data
      var data = jsonDecode(response.body);

      // return the data
      return data;
    }

    return Scaffold(
      appBar: null,
      body: Container(
        padding: const EdgeInsets.fromLTRB(25, 50, 25, 25),
        child: Column(
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
            Text(
              "Server Address: $_serverAddress",
              style: StandardFontStyle.bodyBlack,
            ),

            // Print data
            FutureBuilder(
              future: getData(),
              builder: (context, snapshot) {
                if (snapshot.hasData) {
                  return SingleChildScrollView(
                    child: Text(
                      snapshot.data.toString(),
                      style: StandardFontStyle.captionBlack,
                    ),
                  );
                } else {
                  return const CircularProgressIndicator();
                }
              },
            ),
          ],
        ),
      ),
    );
  }
}
