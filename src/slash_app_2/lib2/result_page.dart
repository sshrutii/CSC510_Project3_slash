import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:html/dom.dart' as dom;
import 'package:url_launcher/url_launcher.dart';

class ResultPage extends StatefulWidget {
  final String selectedValue;
  final String searchText;

  ResultPage(this.selectedValue, this.searchText);

  @override
  _ResultPageState createState() => _ResultPageState();
}

class _ResultPageState extends State<ResultPage> {
  List<SearchResult> searchResults = [];

  @override
  void initState() {
    super.initState();
    fetchSearchResults();
  }

  Future<void> fetchSearchResults() async {
    String searchUrl = getSearchUrl(widget.selectedValue, widget.searchText);
    final response = await http.get(Uri.parse(searchUrl));

    print('Body: ${response.body}');

    dom.Document html = dom.Document.html(response.body);

    final titles = html
        .querySelectorAll('div > div > a > span')
        .map((element) => element.innerHtml.trim())
        .toList();

    print('Count: ${titles.length}');
    for (final title in titles) {
      debugPrint(title);
    }

    final prices = html
        .querySelectorAll('span.f2')
        .map((element) => element.innerHtml.trim())
        .toList();

    print('Count: ${prices.length}');
    for (final price in prices) {
      debugPrint(price);
    }

    final urls = html
        .querySelectorAll('a[href^="/ip/"]')
        .map((element) =>
            'https://www.walmart.com/${element.attributes['href']}')
        .toList();

    print('Count: ${urls.length}');
    for (final url in urls) {
      debugPrint(url);
    }

    final urlImages = html
        .querySelectorAll('.mb0 img')
        .map((element) {
          if ('${element.attributes['src']}'.startsWith('h')) {
            return '${element.attributes['src']}';
          }
        })
        .where((value) => value != null)
        .map((value) => value!)
        .toList();

    print('Count: ${urlImages.length}');
    for (final urlImage in urlImages) {
      debugPrint(urlImage);
    }

    setState(() {
      searchResults = List.generate(
        urls.length,
        (index) => SearchResult(
          title: titles[index],
          price: prices[index],
          url: urls[index],
          imageUrl: urlImages[index]!,
        ),
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Search Results'),
        centerTitle: true,
      ),
      body: ListView.builder(
        padding: EdgeInsets.all(10),
        itemCount: searchResults.length,
        itemBuilder: (context, index) {
          return InkWell(
            onTap: () async {
              launch(searchResults[index].url);
            },
            child: ListTile(
              leading: Image.network(
                searchResults[index].imageUrl,
                width: 50,
                fit: BoxFit.fitHeight,
              ),
              title: Text(
                searchResults[index].title,
                style: TextStyle(fontSize: 10),
              ),
              subtitle: Text('\$${searchResults[index].price}',
                  style: TextStyle(fontWeight: FontWeight.bold, fontSize: 20)),
            ),
          );
        },
      ),
    );
  }

  String getSearchUrl(String selectedValue, String searchText) {
    switch (selectedValue) {
      case 'amazon':
        return 'https://www.amazon.com/s?k=$searchText';
      case 'ebay':
        return 'https://www.ebay.com/sch/i.html?_nkw=$searchText';
      case 'walmart':
        return 'https://www.walmart.com/search?q=$searchText';
      default:
        return 'https://www.google.com/search?q=$searchText';
    }
  }
}

class SearchResult {
  final String title;
  final String price;
  final String url;
  final String imageUrl;

  SearchResult({
    required this.title,
    required this.price,
    required this.url,
    required this.imageUrl,
  });
}
