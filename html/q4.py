import pandas as pd
import qrcode
import cssutils


data = pd.read_csv("AGC4.csv")

style = cssutils.parseString('''
   @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500&family=Roboto:wght@300&display=swap');
        *{
            
            margin: 0%;
            padding: 0%;
        }
    .card {
        border: 1px solid black;
        width: 200px;
        height: 120px;
        margin: 10px;
        padding: 10px;
        text-align: center;
        display: inline-block;
        font-family: Arial, sans-serif;
        height:57vh;
    }
    .name {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .qr {
        margin-top: 10px;
    }
''')

card_html=""
for index, row in data.iterrows():
    # Generate QR code with name and ID
    print(data.CATEGORY)
    qr_data = f'ID:{row["ID"]}, NAME:{row["NAME"]} '
    qr = qrcode.QRCode()
    qr.add_data(qr_data)
    qr.make()
    img = qr.make_image()
    qr_filename = f'{row["ID"]}.png'
    img.save(qr_filename)
    '''
    background:#223BDF
    background:#1ac821
    background:#df2222;
    background:#e85908;
    '''
    if row["CATEGORY"] =="DELEGATE":
      card_html = f'''
       <section style="display: flex;">
        <div style="display:flex;width: 20%;background-color: #223BDF;height:96vh;border-radius: 0% 70% 70% 0%;align-items: center;justify-content: center;">
            <img class="qr" src="{qr_filename}" style="max-width: 100%;">
        </div>
        
        <div style="width: 60%; display: flex; justify-content:flex-end;align-items: center;">
             <div class="name" style="max-height: 94vh;writing-mode: vertical-rl;font-family: 'Montserrat', sans-serif;font-size: xx-large;">
            {row["NAME"]}</div>
            <img src="LOGO_Id.jpeg" alt="" style="width: 48%;padding: 1% 10%;">
        </div> 
        <div style="width: 20%;background-color: #223BDF;height: 96vh;border-radius: 70% 0% 0% 70%; display: flex;justify-content: center;align-items: center;">
        <p style="writing-mode: vertical-rl;font-size: xxx-large;color: white;font-family: 'Montserrat', sans-serif;">DELEGATE</p>
        </div>
    </section>
             '''
  
    elif row["CATEGORY"] =="SPEAKER":
      card_html = f'''
 <section style="display: flex;">
        <div style="display:flex;width: 20%;background-color: #1ac821;height: 96vh;border-radius: 0% 70% 70% 0%;align-items: center;justify-content: center;">
            <img class="qr" src="{qr_filename}" style="max-width: 100%;">
        </div>
        
        <div style="width: 60%; display: flex; justify-content:flex-end;align-items: center;">
             <div class="name" style="max-height: 94vh;writing-mode: vertical-rl;font-family: 'Montserrat', sans-serif;font-size: xx-large;">
            {row["NAME"]}</div>
            <img src="LOGO_Id.jpeg" alt="" style="width: 48%;padding: 1% 10%;">
        </div> 
        <div style="width: 20%;background-color: #1ac821;height: 96vh;border-radius: 70% 0% 0% 70%; display: flex;justify-content: center;align-items: center;">
        <p style="writing-mode: vertical-rl;font-size: xxx-large;color: white;font-family: 'Montserrat', sans-serif;">SPEAKER</p>
        </div>
    </section>
       
    '''
    elif row["CATEGORY"] =="VOLUNTEER":
      card_html = f'''
 <section style="display: flex;">
        <div style="display:flex;width: 20%;background-color: #df2222;height: 96vh;border-radius: 0% 70% 70% 0%;align-items: center;justify-content: center;">
            <img class="qr" src="{qr_filename}" style="max-width: 100%;">
        </div>
        
        <div style="width: 60%; display: flex; justify-content:flex-end;align-items: center;">
             <div class="name" style="max-height: 94vh;writing-mode: vertical-rl;font-family: 'Montserrat', sans-serif;font-size: xx-large;">
            {row["NAME"]}</div>
            <img src="LOGO_Id.jpeg" alt="" style="width: 48%;padding: 1% 10%;">
        </div> 
        <div style="width: 20%;background-color: #df2222;height: 96vh;border-radius: 70% 0% 0% 70%; display: flex;justify-content: center;align-items: center;">
        <p style="writing-mode: vertical-rl;font-size: xxx-large;color: white;font-family: 'Montserrat', sans-serif;">VOLUNTEER</p>
        </div>
    </section>
    '''
    elif row["CATEGORY"] =="ORGANISER":
     card_html = f'''
 <section style="display: flex;">
        <div style="display:flex;width: 20%;background-color: #e85908;height:96vh;border-radius: 0% 70% 70% 0%;align-items: center;justify-content: center;">
            <img class="qr" src="{qr_filename}" style="max-width: 100%;">
        </div>
        
        <div style="width: 60%; display: flex; justify-content:flex-end;align-items: center;">
            <div class="name" style="max-height: 94vh;writing-mode: vertical-rl;font-family: 'Montserrat', sans-serif;font-size: xx-large;">
            {row["NAME"]}</div>
            <img src="LOGO_Id.jpeg" alt="" style="width: 48%;padding: 1% 10%;">
        </div> 
        <div style="width: 20%;background-color: #e85908;height: 96vh;border-radius: 70% 0% 0% 70%; display: flex;justify-content: center;align-items: center;">
        <p style="writing-mode: vertical-rl;font-size: xxx-large;color: white;font-family: 'Montserrat', sans-serif;">ORGANISER</p>
        </div>
    </section>
       
    '''
        
    sheet = cssutils.parseString(f'<style>{style.cssText}</style>')
    card = cssutils.parseString(card_html)
    cssutils.ser.prefs.useMinified()
    cssutils.ser.prefs.omitLastSemicolon = True
    cssutils.ser.prefs.indentBlock = True
    cssutils.ser.prefs.indentSpace = 4
    cssutils.ser.prefs.keepUsedNamespaceDeclarations = True
    cssutils.ser.prefs.quoteSingleDeclarations = True
    cssutils.ser.prefs.quoteNestedDeclarations = True
    cssutils.ser.prefs.keepAllProperties = True
    cssutils.ser.prefs.keepComments = True
    media = cssutils.stylesheets.MediaList('all')
    rule = cssutils.css.CSSStyleRule(selectorText='div.card')
    rule.style.cssText = 'border: 1px solid black; width: 200px; height: 120px; margin: 10px; padding: 10px; text-align: center; display: inline-block; font-family: Arial, sans-serif;'
    sheet.cssRules.insert(0, rule)
    sheet.insertRule(cssutils.css.CSSStyleRule(selectorText='div.name', style='font-size: 24px; font-weight: bold; margin-bottom: 10px;'), 1)
    sheet.insertRule(cssutils.css.CSSStyleRule(selectorText='img.qr', style='margin-top: 10px;'),2)



    with open(f'{row["ID"]}.html', 'w') as f:
        f.write(card_html)
    