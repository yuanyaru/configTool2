module DemoArea {
    sequence<byte> ByteSeq;
    sequence<long> LongSeq;
    sequence<string> StringSeq;
};

module YCArea {
    struct DxPropertyYC {
        int ID;
        string name;
        string describe;
        string unit;
        float kval;
        float bval;
        string address;
        float uplimt;
        float downlimt;
    };

    struct DxDTYC {
        short status;
        float value;
        int timetag;
    };

   sequence<DxPropertyYC> DxPropertyYCSeq;
   sequence<DxDTYC> DxDTYCSeq;
};

module YXArea {
    struct DxPropertyYX {
        int ID;
        string name;
        string describe;
        int ASDU;
        int wordPos;
        int bitPos;
        int bitLength;
        int LinkPoint1;
        int LinkPoint2;
        string OneToZero;
        string ZeroToOne;
        string address;
    };

    struct DxDTYX {
        short status;
        short value;
        int timetag;
    };

   sequence<DxPropertyYX> DxPropertyYXSeq;
   sequence<DxDTYX> DxDTYXSeq;
};

module StationArea {
    struct DxPropertyStation {
        int ID;
        string name;
        string describe;
        int ruleID;
        string address;
        int PORT;
        int role; 
    };
    
    sequence<DxPropertyStation> DxPropertyStationSeq;
};

module SOEArea {
    struct DxPropertySOE {
        int ID;
        string name;
        string describe;
        int level;
        string address;
    };
    sequence<DxPropertySOE> DxPropertySOESeq;
};

module YKArea {
    struct DxPropertyYK {
        int ID;
        string name;
        string describe;
        int ASDU;
        int wordPos;
        int bitPos;
        int bitLength;
        int EnablePoint;
        int EnableValue;
        string address;
    };
    sequence<DxPropertyYK> DxPropertyYKSeq;
};

module YTArea {
    struct DxPropertyYT {
        int ID;
        string name;
        string describe;
        string unit;
        float kval;
        float bval;
        string address;
        float uplimt;
        float downlimt;
    };
    sequence<DxPropertyYT> DxPropertyYTSeq;
};

module CommandArea {
   interface DataCommand {
        int RPCDelYCProperty (int station, DemoArea::LongSeq pIDs);
        int RPCGetYCProperty (int station, out YCArea::DxPropertyYCSeq result);
        int RPCSetYCProperty (int station, YCArea::DxPropertyYCSeq YCProperty);
        int RPCGetRealtimeYCData (int station, DemoArea::LongSeq pIDs, out YCArea::DxDTYCSeq result);
        int RPCGetRealtimeYCDataForHTML (DemoArea::StringSeq pIDs, out YCArea::DxDTYCSeq result);
        int RPCGetDayYCDatas (string datetime, DemoArea::StringSeq pIDs, out DemoArea::LongSeq pIDNum, out YCArea::DxDTYCSeq result, out YCArea::DxDTYCSeq maxseq , out YCArea::DxDTYCSeq minseq, out YCArea::DxDTYCSeq averageseq);
        int RPCGetPeriodYCDatas(string datetime0, string datetime1, DemoArea::StringSeq pIDs, out DemoArea::LongSeq pIDNum, out YCArea::DxDTYCSeq result);       
        int RPCGetTimePointYCData (int station, string datetime, DemoArea::LongSeq pIDs, out YCArea::DxDTYCSeq result);
        int RPCSetRealtimeYCData (int station, DemoArea::LongSeq pIDs, YCArea::DxDTYCSeq data);
        int RPCSaveYCData (int station, DemoArea::LongSeq pIDs, YCArea::DxDTYCSeq data);

        int RPCDelYXProperty (int station, DemoArea::LongSeq pIDs);
        int RPCGetYXProperty (int station, out YXArea::DxPropertyYXSeq result);
        int RPCSetYXProperty (int station, YXArea::DxPropertyYXSeq YXProperty);
        int RPCGetRealtimeYXData (int station, DemoArea::LongSeq pIDs, out YXArea::DxDTYXSeq result);
        int RPCGetRealtimeYXDataForHTML (DemoArea::StringSeq pIDs, out YXArea::DxDTYXSeq result);
        int RPCGetDayYXData (int station, string datetime, long pID, out YXArea::DxDTYXSeq result);
        int RPCGetDayYXDatas (int station, string datetime, DemoArea::LongSeq pIDs, out DemoArea::LongSeq pIDNum, out YXArea::DxDTYXSeq result);
        int RPCGetPeriodYXData(int station, string datetime0,string datetime1, long pID, out YXArea::DxDTYXSeq result);
        int RPCGetTimePointYXData (int station, string datetime, DemoArea::LongSeq pIDs, out YXArea::DxDTYXSeq result);
        int RPCSetRealtimeYXData (int station, DemoArea::LongSeq pIDs, YXArea::DxDTYXSeq data);
        int RPCSaveYXData (int station, DemoArea::LongSeq pIDs, YXArea::DxDTYXSeq data);

        int RPCDelStationProperty (DemoArea::LongSeq stations);
        int RPCGetStationProperty (out StationArea::DxPropertyStationSeq result);
        int RPCSetStationProperty (StationArea::DxPropertyStationSeq StationProperty);

        int RPCDelSOEProperty (int station, DemoArea::LongSeq pIDs);
        int RPCGetSOEProperty (int station, out SOEArea::DxPropertySOESeq result);
        int RPCSetSOEProperty (int station, SOEArea::DxPropertySOESeq SOEProperty);

        int RPCDelYKProperty (int station, DemoArea::LongSeq pIDs);
        int RPCGetYKProperty (int station, out YKArea::DxPropertyYKSeq result);
        int RPCSetYKProperty (int station, YKArea::DxPropertyYKSeq YKProperty);

        int RPCDelYTProperty (int station, DemoArea::LongSeq pIDs);
        int RPCGetYTProperty (int station, out YTArea::DxPropertyYTSeq result);
        int RPCSetYTProperty (int station, YTArea::DxPropertyYTSeq YTProperty);
        
        int RPCGetPropertyTable (out DemoArea::StringSeq stationtable, out DemoArea::StringSeq yctable, out DemoArea::StringSeq yxtable, out DemoArea::StringSeq yktable, out DemoArea::StringSeq yttable, out DemoArea::StringSeq soetable);

    };
};
