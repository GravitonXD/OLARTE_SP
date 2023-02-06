import 'package:flutter/material.dart';
import 'package:alam_app/standards/font_styles.dart';

class DashboardScreen extends StatefulWidget {
  @override
  _DashboardScreenState createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: null,
      body: Center(
        child: Container(
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
                    backgroundColor: Colors.grey[300],
                    child: ClipOval(
                      clipBehavior: Clip.antiAliasWithSaveLayer,
                      child: Image.network(
                          "https://th.bing.com/th/id/OIP.UpfgHT3N1Ao6Juvg1ztmeAHaHa?pid=ImgDet&rs=1"),
                    ),
                  ),
                  // Welcome
                  Text(
                    "Welcome Back, \nMarkton",
                    style: StandardFontStyle.title,
                  )
                ],
              ),
              // Portfolio Bar and Add Button
              Row(
                  // Portfolio Bar
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: [Container()]),
              // Portfolio List Tiles
              Row(),
            ],
          ),
        ),
      ),
    );
  }
}
