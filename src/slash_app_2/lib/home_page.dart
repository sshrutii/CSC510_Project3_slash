import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:slash/result_page.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  List<DropdownMenuItem<String>> get dropdownItems {
    List<DropdownMenuItem<String>> menuItems = [
      const DropdownMenuItem(child: Text("Amazon"), value: "amazon"),
      const DropdownMenuItem(child: Text("CostCo"), value: "costco"),
      const DropdownMenuItem(child: Text("Ebay"), value: "ebay"),
      const DropdownMenuItem(child: Text("Target"), value: "target"),
      const DropdownMenuItem(child: Text("Walmart"), value: "walmart"),
    ];
    return menuItems;
  }

  String selectedValue = "walmart";
  IconData selectedIcon = Icons.search_rounded;
  final _textController = TextEditingController();

  void _navigateToResultScreen() {
    String searchText = _textController.text;
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => ResultPage(selectedValue, searchText),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final mediaQuery = MediaQuery.of(context);
    final Widget pageBody = Container(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          Image.asset('assets/images/slash.png'),
          SizedBox(height: mediaQuery.size.height / 20),
          Container(
            height: mediaQuery.size.height / 12,
            width: mediaQuery.size.width / 3,
            alignment: Alignment.center,
            decoration: BoxDecoration(
              color: Theme.of(context).primaryColor,
              borderRadius: BorderRadius.circular(15),
            ),
            child: DropdownButton(
              alignment: AlignmentDirectional.center,
              borderRadius: BorderRadius.circular(15),
              dropdownColor: Theme.of(context).primaryColorLight,
              elevation: 10,
              iconEnabledColor: Colors.black,
              padding: const EdgeInsets.all(10),
              items: dropdownItems,
              value: selectedValue,
              onChanged: (String? newValue) {
                setState(() {
                  selectedValue = newValue!;
                });
              },
            ),
          ),
          SizedBox(height: mediaQuery.size.height / 20),
          Container(
            width: mediaQuery.size.width / 1.5,
            decoration: BoxDecoration(
              color: Theme.of(context).primaryColor,
              borderRadius: BorderRadius.circular(15),
            ),
            child: TextField(
              controller: _textController,
              textCapitalization: TextCapitalization.sentences,
              autocorrect: true,
              cursorColor: Colors.black,
              showCursor: true,
              onTap: () => setState(() {
                selectedIcon = Icons.clear_rounded;
              }),
              decoration: InputDecoration(
                hintText: 'Search Products...',
                hintStyle: TextStyle(color: Colors.black),
                suffixIcon: IconButton(
                  onPressed: () {
                    _textController.clear();
                  },
                  icon: Icon(selectedIcon),
                ),
                border: InputBorder.none,
                contentPadding: EdgeInsets.all(15),
              ),
            ),
          ),
          SizedBox(height: mediaQuery.size.height / 20),
          Container(
            height: mediaQuery.size.height / 15,
            width: mediaQuery.size.width / 5,
            decoration: BoxDecoration(
              color: Theme.of(context).primaryColor,
              borderRadius: BorderRadius.circular(15),
            ),
            child: TextButton(
              onPressed: _navigateToResultScreen,
              child: const Text(
                'Search',
                style: TextStyle(
                  fontSize: 15,
                  color: Colors.black,
                ),
              ),
            ),
          )
        ],
      ),
    );

    return Platform.isIOS
        ? CupertinoPageScaffold(
            navigationBar: const CupertinoNavigationBar(
              middle: Text('Slash App v2.0'),
            ),
            child: pageBody,
          )
        : Scaffold(
            appBar: AppBar(
              title: const Text('Slash App v2.0'),
              backgroundColor: Theme.of(context).primaryColor,
              foregroundColor: Colors.black,
            ),
            body: pageBody,
          );
  }
}
