import 'package:flutter/material.dart';
import 'package:alam_app/standards/font_styles.dart';

class SellScreen extends StatefulWidget {
  @override
  _SellScreenState createState() => _SellScreenState();
}

class _SellScreenState extends State<SellScreen> {
  // Search Bar Controller
  final searchController = TextEditingController();
  String searchText = "";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: null,
      body: Container(
        padding: const EdgeInsets.fromLTRB(25, 50, 25, 25),
        child: Row(
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
                          "Stocks to Sell",
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
                      print(searchText);
                    },
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
