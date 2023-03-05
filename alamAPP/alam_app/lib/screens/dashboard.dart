import 'package:flutter/material.dart';
import 'package:alam_app/standards/font_styles.dart';
import 'package:lottie/lottie.dart';

class DashboardScreen extends StatefulWidget {
  @override
  _DashboardScreenState createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: null,
      body: Container(
        padding: const EdgeInsets.fromLTRB(25, 50, 25, 25),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: [
            // Welcome Text
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                // Circular Avatar
                CircleAvatar(
                  radius: 45,
                  backgroundColor: const Color.fromARGB(255, 227, 242, 253),
                  child: ClipOval(
                    child: Lottie.asset(
                      'lib/assets/avatar.json',
                    ),
                  ),
                ),
                // Welcome
                Text(
                  "Welcome Back, \nMarkton",
                  style: StandardFontStyle.titleBlack,
                )
              ],
            ),
            // Portfolio Bar and Add Button
            const Divider(
              color: Colors.white,
              height: 30,
            ),
            Row(
              // Portfolio Bar
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
                            const Icon(
                              Icons.work,
                              color: Colors.white,
                              size: 25,
                            ),
                            Text(
                              "Portfolio",
                              style: StandardFontStyle.headingWhite,
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),
                ),
                // Add Button

                GestureDetector(
                  onTap: () => print("Add Button Pressed"),
                  child: const ClipRRect(
                    borderRadius: BorderRadius.all(
                      Radius.circular(20),
                    ),
                    child: SizedBox(
                      width: 55,
                      height: 45,
                      child: ColoredBox(
                        color: Color.fromARGB(255, 129, 199, 132),
                        child: Icon(
                          Icons.add,
                          color: Colors.white,
                          size: 25,
                        ),
                      ),
                    ),
                  ),
                ),
              ],
            ),
            // Portfolio List Tiles
            Row(),

            // UNDER CONSTRUCTION
            SizedBox(
              height: MediaQuery.of(context).size.height * 0.6,
              child: Lottie.asset(
                "lib/assets/underConstruction.json",
              ),
            ),
          ],
        ),
      ),
    );
  }
}
