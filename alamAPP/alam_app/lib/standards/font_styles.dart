// Standards for Font Styles

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class StandardFontStyle {
  static TextStyle title = GoogleFonts.openSans(
    fontSize: 35,
    fontWeight: FontWeight.bold,
    color: Colors.black,
  );

  static TextStyle subtitle = GoogleFonts.openSans(
    fontSize: 18,
    fontWeight: FontWeight.w500,
    color: Colors.black,
  );

  static TextStyle body = GoogleFonts.openSans(
    fontSize: 14,
    fontWeight: FontWeight.w400,
    color: Colors.black,
  );

  static TextStyle caption = GoogleFonts.openSans(
    fontSize: 12,
    fontWeight: FontWeight.w400,
    color: Colors.black,
  );
}
