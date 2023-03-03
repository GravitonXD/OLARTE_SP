// Standards for Font Styles

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class StandardFontStyle {
  static TextStyle titleBlack = GoogleFonts.openSans(
    fontSize: 35,
    fontWeight: FontWeight.bold,
    color: Colors.black,
  );

  static TextStyle titleWhite = GoogleFonts.openSans(
    fontSize: 35,
    fontWeight: FontWeight.bold,
    color: Colors.white,
  );

  static TextStyle headingBlack = GoogleFonts.openSans(
    fontSize: 24,
    fontWeight: FontWeight.w600,
    color: Colors.black,
  );

  static TextStyle headingWhite = GoogleFonts.openSans(
    fontSize: 24,
    fontWeight: FontWeight.w600,
    color: Colors.white,
  );

  static TextStyle subtitleBlack = GoogleFonts.openSans(
    fontSize: 18,
    fontWeight: FontWeight.w500,
    color: Colors.black,
  );

  static TextStyle subtitleWhite = GoogleFonts.openSans(
    fontSize: 18,
    fontWeight: FontWeight.w500,
    color: Colors.white,
  );

  static TextStyle bodyBlack = GoogleFonts.openSans(
    fontSize: 14,
    fontWeight: FontWeight.w400,
    color: Colors.black,
  );

  static TextStyle bodyWhite = GoogleFonts.openSans(
    fontSize: 14,
    fontWeight: FontWeight.w400,
    color: Colors.white,
  );

  static TextStyle captionBlack = GoogleFonts.openSans(
    fontSize: 12,
    fontWeight: FontWeight.w400,
    fontStyle: FontStyle.italic,
    color: Colors.black,
  );

  static TextStyle captionWhite = GoogleFonts.openSans(
    fontSize: 12,
    fontWeight: FontWeight.w400,
    fontStyle: FontStyle.italic,
    color: Colors.white,
  );

  static TextStyle headingGreen = GoogleFonts.openSans(
    fontSize: 24,
    fontWeight: FontWeight.w600,
    color: Colors.green,
  );

  static TextStyle headingRed = GoogleFonts.openSans(
    fontSize: 24,
    fontWeight: FontWeight.w600,
    color: Colors.red,
  );

  static TextStyle chartTitle = GoogleFonts.openSans(
    fontSize: 8,
    fontWeight: FontWeight.w500,
    fontStyle: FontStyle.italic,
    color: Colors.black,
  );
}
