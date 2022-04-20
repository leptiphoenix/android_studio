import 'package:flutter/material.dart';

import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_storage/firebase_storage.dart';

class SearchPage extends StatefulWidget {
  SearchPage({Key? key, required this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  _SearchPageState createState() => _SearchPageState();
}

class _SearchPageState extends State<SearchPage> {
  int _imgcounter = 0;
  int _totalimg = 0;
  int _foundcounter = 0;
  String _status = "Iddle...";

  @override
  void initState() {
    super.initState();
    _status = "Scanning...";
    getRefs();
  }

  var storageRef = FirebaseStorage.instance.ref("generated_photos");

  void getRefs() {
    setState(() {
      storageRef.listAll().then((result) {
        _totalimg = result.items.length;
        _status = "Searching...";
        result.items.forEach((imageRef) {
          // And finally display them
          displayImage(imageRef);
        });
      });
    });
  }

  void displayImage(imageRef) {
    imageRef.getDownloadURL().then((url) {
      //TODO scan the image to search my face here
      setState(() {
        _imgcounter++;
        if (_totalimg==_imgcounter){
          _status = "Done !";
        }
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          // Column is also a layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Invoke "debug painting" (press "p" in the console, choose the
          // "Toggle Debug Paint" action from the Flutter Inspector in Android
          // Studio, or the "Toggle Debug Paint" command in Visual Studio Code)
          // to see the wireframe for each widget.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'Status:',
            ),
            Text(
              '$_status',
              style: Theme.of(context).textTheme.headline4,
            ),
            Text(
              'images checked:',
            ),
            Text(
              '$_imgcounter / ' + (_totalimg == 0 ? '?' : _totalimg.toString()),
              style: Theme.of(context).textTheme.headline4,
            ),
            Text(
              'Your face found:',
            ),
            Text(
              '$_foundcounter',
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
