import 'dart:async';
import 'dart:io';
import 'package:path_provider/path_provider.dart';

class FileProvider {
  late String fileName;

  // Check if file exists
  Future<bool> fileExists() async {
    final file = await _localFile;
    return file.exists();
  }

  Future<String> get _localPath async {
    final directory = await getApplicationDocumentsDirectory();
    return directory.path;
  }

  Future<File> get _localFile async {
    final path = await _localPath;
    return File('$path/$fileName');
  }

  Future<String> readFile() async {
    final file = await _localFile;

    // Read the file
    String serverAddress = await file.readAsString();
    return serverAddress;
  }

  Future<File> writeFile(String serverAddress) async {
    final file = await _localFile;

    // Write the file
    return file.writeAsString(serverAddress);
  }
}
