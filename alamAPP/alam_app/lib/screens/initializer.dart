import 'package:flutter/material.dart';
import 'package:alam_app/standards/font_styles.dart';
import 'package:alam_app/utils/file_provider.dart';

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
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Initializer', style: StandardFontStyle.titleBlack),
      ),
      body: Center(
          child: Column(
        children: [
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
                // Save the server address to a file (json format) in the app documents directory
                widget.serverAddressProvider.writeServerAddress(serverAddress);
                // Go to the home screen
                Navigator.pushNamed(context, '/home');
              },
              child: Text('Confirm', style: StandardFontStyle.bodyWhite),
            ),
          ),
        ],
      )),
    );
  }
}
