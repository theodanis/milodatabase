def main():
    import requests
    from datetime import date, timedelta
    import os
    import json
    
    today = date.today()
    tomorrow = today + timedelta(days=1)
    day_after_tomorrow = today + timedelta(days=2)
    third_day = today + timedelta(days=3)
    
    todayfixture = today.strftime("%Y-%m-%d")
    tomorrowfixture = tomorrow.strftime("%Y-%m-%d")
    otherfixture= day_after_tomorrow.strftime("%Y-%m-%d")
    theotherfixture = third_day.strftime("%Y-%m-%d")
    
    datesAdding = [todayfixture,tomorrowfixture,otherfixture,theotherfixture]
    constant =0
    for dateMine in datesAdding:
        headers = {
            'Authorization': 'Bearer rwIYAI8wzwDBOnNS3HzBKu691nxnbmzxQpwvGyRc5X2g8awo5mh3SlZcSKEh',
        }
        
        response = requests.get(f"https://www.nosyapi.com/apiv2/service/bettable-matches?type=1&date={dateMine}", headers=headers)
        myMatchList = []
        matchData = response.json()['data']
        matchesCount = 0
        for x in range(len(matchData)):
            matchesCount +=1
            print(matchesCount)
            match = matchData[x]
            matchId = match['MatchID']
            response = requests.get(f"https://www.nosyapi.com/apiv2/service/bettable-matches/details?matchID={matchId}apiKey=rwIYAI8wzwDBOnNS3HzBKu691nxnbmzxQpwvGyRc5X2g8awo5mh3SlZcSKEh", headers=headers)
            liste = response.json()['data'][0]['Bets']
            filtered = [g for g in liste if g["gameName"] == 'Karşılıklı Gol']
            if len(filtered)>0:
                newData = filtered[0]['odds']            
                for item in newData:
                    if item["value"] == "Var":
                        kgVar = item["odd"]
                    elif item["value"] == "Yok":
                        kgYok = item["odd"]
            else:
                kgVar=None
                kgYok = None
                  
            filtered = [g for g in liste if g["gameName"] == 'Deplasman İlk Yarı Altı/Üstü 0.5']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "Alt":
                        depI05Y = item["odd"]
                    elif item["value"] == "Üst":
                        depI05V = item["odd"]  
            else:
                depI05V = None
                depI05Y = None 
                 
            filtered = [g for g in liste if g["gameName"] == 'Ev Sahibi İlk Yarı Altı/Üstü 0.5']
            if len(filtered)>0:
                newData = filtered[0]['odds']          
                for item in newData:
                    if item["value"] == "Alt":
                        evI05Y = item["odd"]
                    elif item["value"] == "Üst":
                        evI05V = item["odd"] 
            else:
                evI05V = None
                evI05Y = None
      
            filtered = [g for g in liste if g["gameName"] == 'İlk Yarı Sonucu']
            if len(filtered)>0:
                newData = filtered[0]['odds']
                for item in newData:
                    if item["value"] == "2":
                        iy2 = item["odd"]
                    elif item["value"] == "0":
                        iyX = item["odd"] 
                    elif item["value"] == "1":
                        iy1 = item["odd"]  
            else:
                
                iy1 = None
                iyX = None
                iy2 = None
    
            filtered = [g for g in liste if g["gameName"] == 'Ev Sahibi Gol Yemeden Kazanır']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "Evet":
                        evGolYemedenYes = item["odd"]
                    elif item["value"] == "Hayır":
                        evGolYemedenNo = item["odd"]  
            else:
                evGolYemedenYes = None
                evGolYemedenNo = None 
    
            filtered = [g for g in liste if g["gameName"] == 'Hangi Yarıda Daha Fazla Gol Olur']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "2.":
                        secondPhaseMoreGoal = item["odd"]
                    elif item["value"] == "Eşit":
                        equalGoalonPhase = item["odd"]
                    elif item["value"] == "1.":
                        firstPhaseMoreGoal = item["odd"]                    
            else:
                equalGoalonPhase = None
                firstPhaseMoreGoal = None  
                secondPhaseMoreGoal = None  
    
            filtered = [g for g in liste if g["gameName"] == 'İkinci Yarı Sonucu']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "1":
                        SY1 = item["odd"]
                    elif item["value"] == "0":
                        SYX = item["odd"]
                    elif item["value"] == "2":
                        SY2 = item["odd"]                    
            else:
                SY1 = None
                SYX = None  
                SY2 = None   
    
            filtered = [g for g in liste if g["gameName"] == 'Maç Sonucu ve Alt/Üst 1.5']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "2 ve Üst":
                        u2 = item["odd"]
                    elif item["value"] == "0 ve Üst":
                        u0 = item["odd"]
                    elif item["value"] == "1 ve Üst":
                        u1 = item["odd"]          
                    elif item["value"] == "2 ve Alt":
                        a2 = item["odd"]          
                    elif item["value"] == "0 ve Alt":
                        a0 = item["odd"]          
                    elif item["value"] == "1 ve Alt":
                        a1 = item["odd"]                                     
                                                   
            else:
                a0 = None
                a1 = None  
                a2 = None           
                u0 = None
                u1 = None  
                u2 = None                       
    
            filtered = [g for g in liste if g["gameName"] == 'Ev Sahibi Alt/Üst 2.5']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "Üst":
                        ev25u = item["odd"]
                    elif item["value"] == "Alt":
                        ev25a = item["odd"]               
            else:
                ev25u = None
                ev25a = None  
    
            filtered = [g for g in liste if g["gameName"] == 'Alt/Üst 3.5']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "Üst":
                        total35u = item["odd"]
                    elif item["value"] == "Alt":
                        total35a = item["odd"]               
            else:
                total35u = None
                total35a = None  
    
            filtered = [g for g in liste if g["gameName"] == 'Ev Sahibi Yarı Kazanır']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "Evet":
                        evyarıY = item["odd"]
                    elif item["value"] == "Hayır":
                        evyarıN = item["odd"]               
            else:
                evyarıY = None
                evyarıN = None  
    
            filtered = [g for g in liste if g["gameName"] == 'Deplasman Yarı Kazanır']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "Evet":
                        depyarıY = item["odd"]
                    elif item["value"] == "Hayır":
                        depyarıN = item["odd"]               
            else:
                depyarıY = None
                depyarıN = None  
                
            filtered = [g for g in liste if g["gameName"] == 'Maç Sonucu ve Karşılıklı Gol']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "2 ve Yok":
                        mskg2y = item["odd"]
                    elif item["value"] == "2 ve Var":
                        mskg2v = item["odd"]               
                    elif item["value"] == "0 ve Yok":
                        mskg0y = item["odd"]               
                    elif item["value"] == "0 ve Var":
                        mskg0v = item["odd"]               
                    elif item["value"] == "1 ve Yok":
                        mskg1y = item["odd"]
                    elif item["value"] == "1 ve Var":
                        mskg1v = item["odd"]                    
            else:
                mskg2y = None
                mskg2v = None 
                mskg1y = None
                mskg1v = None 
                mskg0y = None
                mskg0v = None             
    
            filtered = [g for g in liste if g["gameName"] == 'İlk Yarı Karşılıklı Gol']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "Var":
                        iykgy = item["odd"]
                    elif item["value"] == "Yok":
                        iykgn = item["odd"]               
            else:
                iykgy = None
                iykgn = None  
    
            filtered = [g for g in liste if g["gameName"] == 'Alt/Üst 4.5']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "Üst":
                        total45u = item["odd"]
                    elif item["value"] == "Alt":
                        total45a = item["odd"]               
            else:
                total45u = None
                total45a = None
                
            filtered = [g for g in liste if g["gameName"] == 'Deplasman Alt/Üst 1.5']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "Üst":
                        dep15u = item["odd"]
                    elif item["value"] == "Alt":
                        dep15a = item["odd"]               
            else:
                dep15u = None
                dep15a = None   
    
            filtered = [g for g in liste if g["gameName"] == 'Ev Sahibi Alt/Üst 1.5']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "Üst":
                        ev15u = item["odd"]
                    elif item["value"] == "Alt":
                        ev15a = item["odd"]               
            else:
                ev15u = None
                ev15a = None   
    
            filtered = [g for g in liste if g["gameName"] == 'İlk Yarı Alt/Üst 1.5']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "Üst":
                        iy15u = item["odd"]
                    elif item["value"] == "Alt":
                        iy15a = item["odd"]               
            else:
                iy15u = None
                iy15a = None
                
            filtered = [g for g in liste if g["gameName"] == 'İlk Yarı Alt/Üst 0.5']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "Üst":
                        iy05u = item["odd"]
                    elif item["value"] == "Alt":
                        iy05a = item["odd"]               
            else:
                iy05u = None
                iy05a = None   
    
            filtered = [g for g in liste if g["gameName"] == 'Her İki Yarıda da Alt 1.5']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "Evet":
                        bothphasealt15y = item["odd"]
                    elif item["value"] == "Hayır":
                        bothphasealt15n = item["odd"]               
            else:
                bothphasealt15y = None
                bothphasealt15n = None   
                
            filtered = [g for g in liste if g["gameName"] == 'Her İki Yarıda da Üst 1.5']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "Evet":
                        bothphaseust15y = item["odd"]
                    elif item["value"] == "Hayır":
                        bothphaseust15n = item["odd"]               
            else:
                bothphaseust15y = None
                bothphaseust15n = None               
    
            filtered = [g for g in liste if g["gameName"] == 'Maç Sonucu ve Alt/Üst 2.5']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "2 ve Üst":
                        ust2 = item["odd"]
                    elif item["value"] == "0 ve Üst":
                        ust0 = item["odd"]               
                    elif item["value"] == "1 ve Üst":
                        ust1 = item["odd"]               
                    elif item["value"] == "2 ve Alt":
                        alt2 = item["odd"]               
                    elif item["value"] == "0 ve Alt":
                        alt0 = item["odd"]
                    elif item["value"] == "1 ve Alt":
                        alt1 = item["odd"]                    
            else:
                ust2 = None
                ust0 = None 
                ust1 = None
                alt2 = None 
                alt0 = None
                alt1 = None 
            filtered = [g for g in liste if g["gameName"] == 'Altı/Üstü 2.5 ve Karşılıklı Gol']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "Üst ve Yok":
                        yokust = item["odd"]
                    elif item["value"] == "Alt ve Yok":
                        yokalt = item["odd"]               
                    elif item["value"] == "Üst ve Var":
                        varust = item["odd"]               
                    elif item["value"] == "Alt ve Var":
                        varalt = item["odd"]                                 
            else:
                yokust = None
                yokalt = None 
                varust = None
                varalt = None 
    
            filtered = [g for g in liste if g["gameName"] == 'İlk Yarı / Maç Sonucu']
            if len(filtered)>0:
                newData = filtered[0]['odds']        
                for item in newData:
                    if item["value"] == "1/2":
                        to12 = item["odd"]
                    elif item["value"] == "2/2":
                        to22 = item["odd"]               
                    elif item["value"] == "0/2":
                        to02 = item["odd"]               
                    elif item["value"] == "1/1":
                        to11 = item["odd"]               
                    elif item["value"] == "2/1":
                        to21 = item["odd"]
                    elif item["value"] == "0/1":
                        to01 = item["odd"]    
                    elif item["value"] == "1/0":
                        to10 = item["odd"]               
                    elif item["value"] == "2/0":
                        to20 = item["odd"]
                    elif item["value"] == "0/0":
                        to00 = item["odd"]                        
            else:
                to00 = None
                to01 = None 
                to02 = None
                to11 = None 
                to12 = None
                to10 = None
                to21 = None 
                to22 = None
                to20 = None            
    
            result = {
            "homeTeam": match["Team1"],
            "awayTeam": match["Team2"],
            "league": match["League"],
            "time": match["Date"][5:] + " " + match["Time"][:5],  # '09-08 02:00' formatında
            "homeLogo": match["Team1Logo"],
            "awayLogo": match["Team2Logo"],
            "odds": {
                "MS1": match["HomeWin"],
                "MSX": match["Draw"],
                "MS2": match["AwayWin"],
                "2,5 ÜST": match["Over25"],
                "2,5 ALT": match["Under25"],
                "KG VAR": kgVar,
                "KG YOK": kgYok,
                "IY 1": iy1,
                "IY X": iyX,
                "IY 2": iy2,
                "EV IY 0,5 UST":evI05V,
                "EV IY 0,5 ALT":evI05Y,
                "DEP IY 0,5 UST":depI05V,
                "DEP IY 0,5 ALT":depI05Y,  
                "EV GOL YEMEDEN KAZANIR:EVET" :evGolYemedenYes,
                "EV GOL YEMEDEN KAZANIR:HAYIR":evGolYemedenNo,
                "HANGİ YARI DAHA FAZLA GOL OLUR:1.":firstPhaseMoreGoal,
                "HANGİ YARI DAHA FAZLA GOL OLUR:EŞİT":equalGoalonPhase,
                "HANGİ YARI DAHA FAZLA GOL OLUR:2.":secondPhaseMoreGoal,
                "İKİNCİ YARI SONUCU:1":SY1,
                "İKİNCİ YARI SONUCU:X":SYX,
                "İKİNCİ YARI SONUCU:2":SY2,
                "MSX 1,5 ALT":a0,
                "MS1 1,5 ALT":a1,
                "MS2 1,5 ALT":a2,
                "MSX 1,5 UST":u0,
                "MS1 1,5 UST":u1,
                "MS2 1,5 UST":u2,   
                "EV SAHIBI 2,5 UST": ev25u,
                "EV SAHIBI 2,5 ALT": ev25a,
                "3,5 UST":total35u,
                "3,5 ALT":total35a,
                "EV SAHİBİ YARI KAZANIR:EVET" :evyarıY,
                "EV SAHİBİ YARI KAZANIR:HAYRI" :evyarıN,
                "DEPLASMAN YARI KAZANIR:EVET" :depyarıY,
                "DEPLASMAN YARI KAZANIR:HAYIR" :depyarıN,
                "MS 1 KG VAR" :mskg1v,   
                "MS 0 KG VAR" :mskg0v,   
                "MS 2 KG VAR" :mskg2v,   
                "MS 1 KG YOK" :mskg1y,   
                "MS 0 KG YOK" :mskg0y,   
                "MS 2 KG YOK" :mskg2y, 
                "İLK YARI KARŞILIKLI GOL VAR":iykgy,
                "İLK YARI KARŞILIKLI GOL YOK":iykgn,
                "4,5 UST":total45u,
                "4,5 ALT":total45a,
                "DEPLASMAN 1,5 UST":dep15u,
                "DEPLASMAN 1,5 ALT":dep15a,
                "EV SAHİBİ 1,5 UST":ev15u,
                "EV SAHİBİ 1,5 ALT":ev15a,
                "İLK YARI 1,5 ÜST":iy15u,
                "İLK YARI 1,5 ALT":iy15a,  
                "İLK YARI 0,5 ÜST":iy05u,
                "İLK YARI 0,5 ALT":iy05a,
                "HER İKİ YARI DA 1,5 ALT:EVET":bothphasealt15y,
                "HER İKİ YARI DA 1,5 ALT:HAYIR":bothphasealt15n,
                "HER İKİ YARI DA 1,5 ÜST:EVET":bothphaseust15y,
                "HER İKİ YARI DA 1,5 ÜST:HAYIR":bothphaseust15n,   
                "MS1 2,5 ÜST":ust1,   
                "MS2 2,5 ÜST":ust2,   
                "MSX 2,5 ÜST":ust0,   
                "MS1 2,5 ALT":alt1,   
                "MS2 2,5 ALT":alt2,   
                "MSX 2,5 ALT":alt0,
                "2,5 ÜST KG VAR":varust,
                "2,5 ÜST KG YOK":yokust,
                "2,5 ALT KG VAR":varalt,
                "2,5 ALT KG YOK":yokalt,
                "İY/MS:X/X":to00,
                "İY/MS:X/1":to01,
                "İY/MS:X/2":to02,
                "İY/MS:1/X":to10,
                "İY/MS:1/1":to11,
                "İY/MS:1/2":to12,
                "İY/MS:2/X":to20,
                "İY/MS:2/1":to21,
                "İY/MS:2/2":to22
                
            }
        }
            myMatchList.append(result)
    
                
        
        for m in myMatchList:
            m["time"] = "2025-" + m["time"]
        
        
        from datetime import datetime
        from collections import defaultdict
        
        # Gün bazında gruplayacağımız dict
        matches_by_day = defaultdict(list)
        
        for match in myMatchList:
            day_str = datetime.fromisoformat(match['time']).date().isoformat()  # '2025-08-24'
            matches_by_day[day_str].append(match)
        
        # İstenilen formatta dict
        grouped_matches = {day: {"matches": matches} for day, matches in matches_by_day.items()}
        
        for day, data in grouped_matches.items():
            for match in data['matches']:
                dt = datetime.fromisoformat(match['time'].replace('Z',''))  # UTC+0 ise Z eklenmiş olabilir
                match['time'] = dt.strftime("%d-%m %H:%M")  # "Gün-Ay Saat:Minute"
        
        import firebase_admin
        from firebase_admin import credentials, firestore
        
        #Firestore bağlantısı
        if constant ==0:
            cred = credentials.Certificate("burakdenemeserdar-firebase-adminsdk-fbsvc-b78b572f0e.json")  # kendi json key dosyan
            firebase_admin.initialize_app(cred)
            db = firestore.client()
        else:
            pass
        
        #Önce Sil
        from google.cloud import firestore
        
        for x in range(len(grouped_matches.keys())):
            db.collection("matches").document(list(grouped_matches.keys())[x]).delete()
        
        for x in range(len(grouped_matches)):
            tarih = list(grouped_matches.keys())[x]
            dictData = list(grouped_matches.values())[x] 
            
            data = {tarih:dictData}
        
        
        # Bulk yükleme
        for match_date, games in data.items():
            db.collection("matches").document(match_date).set({
                "events": games
            })
    
        constant +=1
            
        
            
        
    ##TAKIM STATS
    
    import firebase_admin
    from firebase_admin import credentials, firestore
    from datetime import datetime
    import pytz
    
    # Firestore başlat
    #cred = credentials.Certificate(""/etc/secrets/firebase_key.json"")
    #firebase_admin.initialize_app(cred)
    #db = firestore.client()
    
    # Türkiye timezone
    tz = pytz.timezone("Europe/Istanbul")
    today = datetime.now(tz).date()  # sadece YYYY-MM-DD formatı için
    
    distinct_teams = set()
    
    # 1️⃣ matches koleksiyonundaki tüm dokümanları al
    docs = db.collection("matches").stream()
    
    for doc in docs:
        doc_date_str = doc.id  # Örn: "2025-09-10"
        try:
            doc_date = datetime.strptime(doc_date_str, "%Y-%m-%d").date()
        except ValueError:
            continue  # ID tarih formatında değilse atla
    
        # 2️⃣ Sadece bugünden sonraki tarihler
        if doc_date >= today:
            data = doc.to_dict()
            matches_list = data.get("events", {}).get("matches", [])
    
            for match in matches_list:
                home_team = match.get("homeTeam")
                away_team = match.get("awayTeam")
                if home_team:
                    distinct_teams.add(home_team)
                if away_team:
                    distinct_teams.add(away_team)
    
    country_map = {
        "Türkiye": "Turkey",
        "Almanya": "Germany",
        "İngiltere": "England",
        "İtalya": "Italy",
        "Fransa": "France",
        "İspanya": "Spain",
        "Portekiz": "Portugal",
        "Hollanda": "Netherlands",
        "Belçika": "Belgium",
        "Yunanistan": "Greece",
        "Rusya": "Russia",
        "İsviçre": "Switzerland",
        "Avusturya": "Austria",
        "Avustralya": "Australia",
        "İsveç": "Sweden",
        "Norveç": "Norway",
        "Danimarka": "Denmark",
        "Finlandiya": "Finland",
        "İrlanda": "Ireland",
        "Polonya": "Poland",
        "Ukrayna": "Ukraine",
        "Romanya": "Romania",
        "Macaristan": "Hungary",
        "Çekya": "Czech Republic",
        "Slovakya": "Slovakia",
        "Hırvatistan": "Croatia",
        "Sırbistan": "Serbia",
        "Bulgaristan": "Bulgaria",
        "Slovenya": "Slovenia",
        "Sırbistan": "Serbia",
        "Kosova": "Kosovo",
        "Litvanya": "Lithuania",
        "Letonya": "Latvia",
        "Estonya": "Estonia",
        "Belarus": "Belarus",
        "Bosna Hersek": "Bosnia and Herzegovina",
        "Arnavutluk": "Albania",
        "Moldova": "Moldova",
        "Karadağ": "Montenegro",
        "Kuzey Makedonya": "North Macedonia",
        "Slovakya": "Slovakia",
        "İzlanda": "Iceland",
        "San Marino": "San Marino",
        "Andorra": "Andorra",
        "Lüksemburg": "Luxembourg",
        "Liechtenstein": "Liechtenstein",
        "Galler": "Wales",
        "İskoçya": "Scotland",
        "Kuzey İrlanda": "Northern Ireland",
        "Gürcistan": "Georgia",
        "Ermenistan": "Armenia",
        "Azerbaycan": "Azerbaijan",
        "Kazakistan": "Kazakhstan",
        "Türkmenistan": "Turkmenistan",
        "Kırgızistan": "Kyrgyzstan",
        "Özbekistan": "Uzbekistan",
        "Tacikistan": "Tajikistan",
        "Afganistan": "Afghanistan",
        "Paşistan": "Pakistan",
        "Hindistan": "India",
        "Bangladeş": "Bangladesh",
        "Sri Lanka": "Sri Lanka",
        "Nepal": "Nepal",
        "Butan": "Bhutan",
        "Maldivler": "Maldives",
        "Mısır": "Egypt",
        "Fas": "Morocco",
        "Cezayir": "Algeria",
        "Tunus": "Tunisia",
        "Libya": "Libya",
        "Sudan": "Sudan",
        "Senegal": "Senegal",
        "Gana": "Ghana",
        "Kamerun": "Cameroon",
        "Nijerya": "Nigeria",
        "Ethiopya": "Ethiopia",
        "Uganda": "Uganda",
        "Zambiya": "Zambia",
        "Zimbabve": "Zimbabwe",
        "Kenya": "Kenya",
        "Meksika": "Mexico",
        "Brezilya": "Brazil",
        "Arjantin": "Argentina",
        "Kolombiya": "Colombia",
        "Şili": "Chile",
        "Peru": "Peru",
        "Venezuela": "Venezuela",
        "Paraguay": "Paraguay",
        "Uruguay": "Uruguay",
        "Bolivya": "Bolivia",
        "Ekvador": "Ecuador",
        "Kosta Rika": "Costa Rica",
        "Panama": "Panama",
        "Güney Afrika": "South Africa",
        "Yeni Zelanda": "New Zealand",
        "Singapur": "Singapore",
        "Malezya": "Malaysia",
        "Endonezya": "Indonesia",
        "Filipinler": "Philippines",
        "Japonya": "Japan",
        "Güney Kore": "South Korea",
        "Çin": "China",
        "Tayland": "Thailand",
        "Vietnam": "Vietnam",
        "Tayvan": "Taiwan",
        "Birleşik Arap Emirlikleri": "United Arab Emirates",
        "Katar": "Qatar",
        "Suudi Arabistan": "Saudi Arabia",
        "İran": "Iran",
        "Irak": "Iraq",
        "Ürdün": "Jordan",
        "İsrail": "Israel",
        "Lübnan": "Lebanon",
        "Kuveyt": "Kuwait",
        "Faroe Adaları":"Faroe Islands",
        "Kanada":"Canada",
        "Cebelitarık":"Gibraltar",
        "Mozambik":"Mozambique"
    }
    # İngilizceye çevirme
    translated_teams = set()
    for team in distinct_teams:
        # Ülke adı country_map içinde geçen kısmını bul
        replaced = team
        for turkce, ingilizce in country_map.items():
            if team.startswith(turkce):
                replaced = team.replace(turkce, ingilizce, 1)
                break
        translated_teams.add(replaced)
    
    
    import requests
    
    API_KEY = "8fdf966e420f7033fc4a1a93ad6a095b"
    SEASON = 2025
    headers = {"x-apisports-key": API_KEY}
    
    def get_team_stats_by_name(team_name, last_n=5):
        # 1️⃣ Takım ID bul
        url = "https://v3.football.api-sports.io/teams"
        params = {"search": team_name}
        r = requests.get(url, headers=headers, params=params)
        data = r.json()
        if not data["response"]:
            return {"error": f"{team_name} bulunamadı ❌"}
        
        team_id = data["response"][0]["team"]["id"]
        real_name = data["response"][0]["team"]["name"]
    
        # 2️⃣ Son maçları al
        url = "https://v3.football.api-sports.io/fixtures"
        params = {"team": team_id, "last": last_n}
        r = requests.get(url, headers=headers, params=params)
        matches_data = r.json().get("response", [])
    
        total_wins, total_draws, total_losses = 0, 0, 0
        goals_for, goals_against = 0, 0
        form = ""
        last_matches = {}
    
        for match in matches_data:
            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]
            home_id = match["teams"]["home"]["id"]
            away_id = match["teams"]["away"]["id"]
            home_score = match["goals"]["home"] or 0
            away_score = match["goals"]["away"] or 0
    
            last_matches[f"{home} - {away}"] = f"{home_score}-{away_score}"
    
            if home_id == team_id:
                goals_for += home_score
                goals_against += away_score
                if match["teams"]["home"]["winner"]:
                    total_wins += 1
                    form += "W"
                elif home_score == away_score:
                    total_draws += 1
                    form += "D"
                else:
                    total_losses += 1
                    form += "L"
            else:
                goals_for += away_score
                goals_against += home_score
                if match["teams"]["away"]["winner"]:
                    total_wins += 1
                    form += "W"
                elif home_score == away_score:
                    total_draws += 1
                    form += "D"
                else:
                    total_losses += 1
                    form += "L"
    
        # 3️⃣ Sakat oyuncular
        url = "https://v3.football.api-sports.io/players"
        params = {"team": team_id, "season": SEASON}
        r = requests.get(url, headers=headers, params=params)
        players_data = r.json().get("response", [])
        injured_players = [p["player"]["name"] for p in players_data if p.get("player", {}).get("injured") == True]
    
        # 4️⃣ Sonuç
        return {
            "team": real_name,
            "son5maç_galibiyet": total_wins,
            "son5maç_beraberlik": total_draws,
            "son5maç_mağlubiyet": total_losses,
            "attığı_gol": goals_for,
            "yediği_gol": goals_against,
            "form": form,
            "oynadığı_maçlar": last_matches,
            "sakat_sayısı": len(injured_players)
        }
    
    
    # 🔍 Örnek kullanım
    stats = get_team_stats_by_name("Slovenia U21")
    
    import firebase_admin
    from firebase_admin import credentials, firestore
    import time
    
    # --- Firebase Admin başlat ---
    #cred = credentials.Certificate(""/etc/secrets/firebase_key.json"")
    #firebase_admin.initialize_app(cred)
    #db = firestore.client()
    
    # Her takım için istatistikleri al ve Firestore'a yaz
    for idx, team_name in enumerate(translated_teams, start=1):
        stats = get_team_stats_by_name(team_name)
    
        if "error" in stats:
            print(stats["error"])
            continue  # Takım bulunamazsa geç
    
        # 2️⃣ Yeni veriyi ekle
        try:
            db.collection("team_stats").document(stats["team"]).set(stats)
            print(f"{stats['team']} Firestore'a eklendi ✅")
        except:
            pass
        
    
        # API limitine takılmamak için 1 saniye bekle
    
    print("Tüm takımların istatistikleri Firestore'a kaydedildi ✅")
    
    ##THINKINGS
    
    import firebase_admin
    from firebase_admin import credentials, firestore
    
    # --- Firebase Admin başlat ---
    #cred = credentials.Certificate(""/etc/secrets/firebase_key.json"")
    #firebase_admin.initialize_app(cred)
    #db = firestore.client()
    
    
    # 1️⃣ İngilizce → Türkçe mapping
    english_to_turkish = {v: k for k, v in country_map.items()}
    
    # 2️⃣ team_stats koleksiyonunu çek
    teams_stats_docs = db.collection("team_stats").stream()
    
    for doc in teams_stats_docs:
        team_stats = doc.to_dict()
        team_name_eng = team_stats["team"]
    
        # Doküman adını Türkçe yap
        team_name_tr = english_to_turkish.get(team_name_eng, team_name_eng)
    
        # 1️⃣ Son 5 maç galibiyet
        info1 = f"{team_name_tr} son 5 maçında {team_stats['son5maç_galibiyet']} galibiyet aldı."
    
        # 2️⃣ Son 5 maçta karşılıklı gol
        cg_count = 0
        last5_matches = list(team_stats.get("oynadığı_maçlar", {}).values())[:5]
        for score in last5_matches:
            try:
                home_goals, away_goals = map(int, score.split("-"))
                if home_goals > 0 and away_goals > 0:
                    cg_count += 1
            except:
                continue
        info2 = f"{team_name_tr} son 5 maçının {cg_count} maçında karşılıklı gol oldu."
    
        # 3️⃣ Son 3 maçta attığı ve yediği gol
        last3_matches = list(team_stats.get("oynadığı_maçlar", {}).values())[:3]
        goals_for, goals_against = 0, 0
        for score in last3_matches:
            try:
                home_goals, away_goals = map(int, score.split("-"))
                if "home" in score.lower():  # ev sahibi ise
                    goals_for += home_goals
                    goals_against += away_goals
                else:
                    goals_for += away_goals
                    goals_against += home_goals
            except:
                continue
        info3 = f"{team_name_tr} son 3 maçta toplam {goals_for} gol atarken {goals_against} gol yedi."
    
        # Firestore'a yaz
        db.collection("teamstats_info").document(team_name_tr).set({
            "info1": info1,
            "info2": info2,
            "info3": info3
        })
if __name__ == "__main__":
    main()
