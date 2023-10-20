import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:html/dom.dart' as dom;
import 'package:url_launcher/url_launcher.dart';
import "dart:math";

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

    var titles = [];
    var prices;
    var urls;
    var urlImages;

    switch (widget.selectedValue) {
      case 'costco':
        titles = html
            .querySelectorAll('span > a')
            .map((element) => element.innerHtml.trim())
            .toList();

        prices = html
            .querySelectorAll('div.price')
            .map((element) => element.innerHtml.trim().substring(1))
            .toList();

        urls = html
            .querySelectorAll('span > a')
            .map((element) => '${element.attributes['href']}')
            .toList();

        urlImages = html
            .querySelectorAll('img[automation-id^="productImageLink_"]')
            .map((element) {
              if ('${element.attributes['src']}'.startsWith('h')) {
                return '${element.attributes['src']}';
              }
            })
            .where((value) => value != null)
            .map((value) => value!)
            .toList();
      case 'ebay':
      case 'walmart':
        titles = html
            .querySelectorAll('div > div > a > span')
            .map((element) => element.innerHtml.trim())
            .toList();

        prices = html
            .querySelectorAll('span.f2')
            .map((element) => element.innerHtml.trim())
            .toList();

        urls = html
            .querySelectorAll('a[href^="/ip/"]')
            .map((element) =>
                'https://www.walmart.com/${element.attributes['href']}')
            .toList();

        urlImages = html
            .querySelectorAll('.mb0 img')
            .map((element) {
              if ('${element.attributes['src']}'.startsWith('h')) {
                return '${element.attributes['src']}';
              }
            })
            .where((value) => value != null)
            .map((value) => value!)
            .toList();
      default:
    }

    print('Count: ${titles.length}');
    for (final title in titles) {
      debugPrint(title);
    }
    print('Count: ${prices.length}');
    for (final price in prices) {
      debugPrint(price);
    }
    print('Count: ${urls.length}');
    for (final url in urls) {
      debugPrint(url);
    }
    print('Count: ${urlImages.length}');
    for (final urlImage in urlImages) {
      debugPrint(urlImage);
    }

    List<int> lengths = [
      titles.length,
      prices.length,
      urls.length,
      urlImages.length
    ];
    int smallestLength = lengths.reduce(min);

    setState(() {
      searchResults = List.generate(
        smallestLength,
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
      case 'costco':
        return 'https://www.costco.com/CatalogSearch?dept=All&keyword=$searchText';
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
