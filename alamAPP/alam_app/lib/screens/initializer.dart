import 'package:flutter/material.dart';
import 'package:alam_app/standards/font_styles.dart';
import 'package:alam_app/utils/file_provider.dart';
import 'package:http/http.dart' as http;

class Initializer extends StatefulWidget {
  late final ServerAddressProvider serverAddressProvider;

  @override
  _InitializerState createState() => _InitializerState();
}

class _InitializerState extends State<Initializer> {
  String serverAddress = "";

  @override
  void initState() {
    super.initState();
    widget.serverAddressProvider = ServerAddressProvider();

    // Check if server address is already saved
    Future<void> checkFile() async {
      if (await widget.serverAddressProvider.fileExists()) {
        widget.serverAddressProvider.readFile().then((value) {
          setState(() {
            serverAddress = value;
          });
        });
      }
    }

    checkFile();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: true,
      appBar: AppBar(
        title: Text(
          'alamAPP Initializer',
          style: StandardFontStyle.titleWhite,
        ),
        centerTitle: true,
        actions: [
          // Info button
          IconButton(
            icon: const Icon(
              Icons.info_outline,
              color: Colors.white,
            ),
            onPressed: () {
              showDialog(
                context: context,
                builder: (BuildContext context) {
                  return AlertDialog(
                    title: Text(
                      'Info',
                      style: StandardFontStyle.titleBlack,
                    ),
                    content: Text(
                      'alamAPP is a test mobile-based application that allows users to see the forecasted prices of 20 different market in the Philippine Stock Market, specifically each stocks are categorized to buy and to sell. This application is designed to be used in conjunction with the alamAPI, which is part of the alamSYS.',
                      style: StandardFontStyle.bodyBlack,
                      textAlign: TextAlign.justify,
                    ),
                    actions: [
                      TextButton(
                        onPressed: () {
                          Navigator.of(context).pop();
                        },
                        child: Text('OK', style: StandardFontStyle.bodyBlack),
                      ),
                    ],
                  );
                },
              );
            },
          ),
        ],
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // Photo
            Container(
              padding: const EdgeInsets.all(10),
              width: MediaQuery.of(context).size.width * 0.8,
              child: Image.asset('lib/assets/initializer_img.png'),
            ),
            // Input Bar for IP address of the server
            Container(
              padding: const EdgeInsets.all(10),
              width: MediaQuery.of(context).size.width * 0.8,
              child: TextField(
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: 'Server IPv4 Address',
                ),
                onChanged: (text) {
                  serverAddress = text;
                },
              ),
            ),
            // Confirm Button (Continues to the home screen and passes the server address)
            Container(
              padding: const EdgeInsets.all(10),
              width: MediaQuery.of(context).size.width * 0.8,
              child: ElevatedButton(
                onPressed: () {
                  // Check if the server address is valid
                  /*
                    Valid IPv4 address:
                    - Not empty
                    - Contains only numbers and dots
                  */
                  if (serverAddress == "" ||
                      !RegExp(r'^[0-9.]+$').hasMatch(serverAddress)) {
                    showDialog(
                      context: context,
                      builder: (BuildContext context) {
                        return AlertDialog(
                          title: Text(
                            'Error',
                            style: StandardFontStyle.titleBlack,
                          ),
                          content: Text(
                            'Please enter a valid IPv4 address.',
                            style: StandardFontStyle.bodyBlack,
                            textAlign: TextAlign.justify,
                          ),
                          actions: [
                            TextButton(
                              onPressed: () {
                                Navigator.of(context).pop();
                              },
                              child: Text('OK',
                                  style: StandardFontStyle.bodyBlack),
                            ),
                          ],
                        );
                      },
                    );
                    return;
                  }
                  // Save the server address to a file in the app documents directory
                  widget.serverAddressProvider.writeFile(serverAddress);
                  // Go to the home screen
                  Navigator.pushNamed(context, '/home');
                },
                child: Text('Confirm', style: StandardFontStyle.bodyWhite),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
