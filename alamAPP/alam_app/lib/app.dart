import 'package:flutter/material.dart';
import 'package:alam_app/screens/home.dart';

class AlamApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Alam',
      theme: _alamAppTheme,
      initialRoute: '/home',
      routes: {
        '/home': (context) => Home(),
      },
    );
  }
}

final ThemeData _alamAppTheme = _buildAlamAppTheme();
final ColorScheme _alamAppColorScheme = _buildAlamAppColorScheme();

ThemeData _buildAlamAppTheme() {
  final ThemeData base = ThemeData.light();
  return base.copyWith(
    visualDensity: VisualDensity.adaptivePlatformDensity,
    colorScheme: _alamAppColorScheme,
  );
}

ColorScheme _buildAlamAppColorScheme() {
  return const ColorScheme(
    brightness: Brightness.light,
    primary: Color.fromARGB(255, 66, 165, 245),
    onPrimary: Colors.white,
    secondary: Color.fromARGB(255, 171, 71, 188),
    onSecondary: Colors.white,
    error: Color.fromARGB(255, 229, 115, 115),
    onError: Colors.white,
    background: Colors.white,
    onBackground: Colors.black,
    surface: Colors.white,
    onSurface: Colors.black,
  );
}
