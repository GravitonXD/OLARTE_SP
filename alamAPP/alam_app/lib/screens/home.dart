import 'package:alam_app/utils/file_provider.dart';
import 'package:flutter/material.dart';
import 'package:alam_app/screens/dashboard.dart';
import 'package:alam_app/screens/to_buy.dart';
import 'package:alam_app/screens/to_sell.dart';

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  // Initialized Bottom Navigation Counter to 0 : Dashboard
  int _bottomNavPage = 0;
  final List<Widget> _screens = [
    DashboardScreen(),
    BuyScreen(),
    SellScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: false,
      body: Center(
        child: _screens[_bottomNavPage],
      ),
      bottomNavigationBar: NavigationBarTheme(
        data: const NavigationBarThemeData(
          indicatorColor: Color.fromARGB(255, 66, 165, 245),
          labelBehavior: NavigationDestinationLabelBehavior.alwaysHide,
          indicatorShape: RoundedRectangleBorder(
            borderRadius: BorderRadius.all(
              Radius.circular(20),
            ),
          ),
        ),
        child: NavigationBar(
          backgroundColor: const Color.fromARGB(255, 227, 242, 253),
          animationDuration: const Duration(milliseconds: 500),
          labelBehavior: NavigationDestinationLabelBehavior.onlyShowSelected,
          height: 75,
          selectedIndex: _bottomNavPage,
          onDestinationSelected: (int newIndex) {
            setState(() {
              _bottomNavPage = newIndex;
            });
          },
          destinations: [
            NavigationDestination(
              icon: Icon(
                Icons.account_circle_outlined,
                color: _bottomNavPage == 0 ? Colors.white : Colors.black,
                size: 30,
              ),
              label: 'Dashboard',
            ),
            NavigationDestination(
              icon: Icon(
                Icons.trending_up_rounded,
                color: _bottomNavPage == 1 ? Colors.white : Colors.black,
                size: 30,
              ),
              label: 'Buy',
            ),
            NavigationDestination(
              icon: Icon(
                Icons.trending_down_rounded,
                color: _bottomNavPage == 2 ? Colors.white : Colors.black,
                size: 30,
              ),
              label: 'Sell',
            ),
          ],
        ),
      ),
    );
  }
}
