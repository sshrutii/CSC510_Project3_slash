import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:slash/result_page.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  List<DropdownMenuItem<String>> get dropdownItems {
    return [
      DropdownMenuItem(child: Text(" Amazon"), value: "amazon"),
      DropdownMenuItem(child: Text(" CostCo"), value: "costco"),
      DropdownMenuItem(child: Text(" Ebay"), value: "ebay"),
      DropdownMenuItem(child: Text(" Target"), value: "target"),
      DropdownMenuItem(child: Text(" Walmart"), value: "walmart"),
    ];
  }

  String selectedValue = " walmart";
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
    final ThemeData theme = Theme.of(context);

    return Platform.isIOS
        ? CupertinoPageScaffold(
      navigationBar: CupertinoNavigationBar(
        middle: Text('Slash App v2.0'),
      ),
      child: _buildHomePage(mediaQuery, theme),
    )
        : Scaffold(
      appBar: AppBar(
        title: Text('Slash App v2.0'),
        backgroundColor: theme.primaryColor,
      ),
      body: _buildHomePage(mediaQuery, theme),
    );
  }

  Widget _buildHomePage(MediaQueryData mediaQuery, ThemeData theme) {
    return Stack(
      children: [
        // Background Image
        Positioned.fill(
          child: Image.asset(
            'assets/images/bg2.png', // Replace with your image path
            fit: BoxFit.cover,
          ),
        ),
        Container(
          padding: EdgeInsets.all(20),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Image.asset('assets/images/slashtxt1.png'),
              SizedBox(height: 20),
              Container(
                width: mediaQuery.size.width / 2,
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(15),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.grey.withOpacity(0.5),
                      spreadRadius: 3,
                      blurRadius: 7,
                      offset: Offset(0, 3),
                    ),
                  ],
                ),
                child: DropdownButton(
                  isExpanded: true,
                  icon: Icon(Icons.arrow_drop_down),
                  iconSize: 32,
                  underline: SizedBox(),
                  items: dropdownItems,
                  value: selectedValue,
                  onChanged: (String? newValue) {
                    setState(() {
                      selectedValue = newValue!;
                    });
                  },
                ),
              ),
              SizedBox(height: 20),
              Container(
                width: mediaQuery.size.width / 1.5,
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(15),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.grey.withOpacity(0.5),
                      spreadRadius: 3,
                      blurRadius: 7,
                      offset: Offset(0, 3),
                    ),
                  ],
                ),
                child: TextField(
                  controller: _textController,
                  textCapitalization: TextCapitalization.sentences,
                  autocorrect: true,
                  cursorColor: Colors.black,
                  decoration: InputDecoration(
                    hintText: 'Search Products...',
                    hintStyle: TextStyle(color: Colors.grey),
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
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: _navigateToResultScreen,
                style: ElevatedButton.styleFrom(
                  primary: theme.primaryColor,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(15),
                  ),
                ),
                child: Padding(
                  padding: EdgeInsets.symmetric(vertical: 15, horizontal: 30),
                  child: Text(
                    'Search',
                    style: TextStyle(
                      fontSize: 18,
                      color: Colors.white,
                    ),
                  ),
                ),
              )
            ],
          ),
        ),
      ],
    );
  }
}

