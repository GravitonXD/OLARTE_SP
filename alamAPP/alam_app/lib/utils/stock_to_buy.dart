class BuyParser {
  List<Stocks>? stocks;

  BuyParser({this.stocks});

  BuyParser.fromJson(Map<String, dynamic> json) {
    if (json['Stocks'] != null) {
      stocks = <Stocks>[];
      json['Stocks'].forEach((v) {
        stocks!.add(new Stocks.fromJson(v));
      });
    }
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    if (this.stocks != null) {
      data['Stocks'] = this.stocks!.map((v) => v.toJson()).toList();
    }
    return data;
  }
}

class Stocks {
  Id? iId;
  String? stockSymbol;
  double? lastClosing;
  PredictedClosing? predictedClosing;

  Stocks({this.iId, this.stockSymbol, this.lastClosing, this.predictedClosing});

  Stocks.fromJson(Map<String, dynamic> json) {
    iId = json['_id'] != null ? new Id.fromJson(json['_id']) : null;
    stockSymbol = json['stock_symbol'];
    lastClosing = json['last_closing'];
    predictedClosing = json['predicted_closing'] != null
        ? new PredictedClosing.fromJson(json['predicted_closing'])
        : null;
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    if (this.iId != null) {
      data['_id'] = this.iId!.toJson();
    }
    data['stock_symbol'] = this.stockSymbol;
    data['last_closing'] = this.lastClosing;
    if (this.predictedClosing != null) {
      data['predicted_closing'] = this.predictedClosing!.toJson();
    }
    return data;
  }
}

class Id {
  String? oid;

  Id({this.oid});

  Id.fromJson(Map<String, dynamic> json) {
    oid = json['$oid'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['$oid'] = this.oid;
    return data;
  }
}

class PredictedClosing {
  List<double>? dmdLstm;

  PredictedClosing({this.dmdLstm});

  PredictedClosing.fromJson(Map<String, dynamic> json) {
    dmdLstm = json['dmd_lstm'].cast<double>();
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['dmd_lstm'] = this.dmdLstm;
    return data;
  }
}
