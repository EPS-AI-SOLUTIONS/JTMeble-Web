import json
import random

file_path = r"C:\Users\BIURODOM\Desktop\JTMeble-Web\src\data\scraped_products.json"

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

templates = {
    "Biurka i stoły": [
        "Inwestuj w efektywność i ergonomię dzięki {name}. Ten model to gwarancja optymalnej przestrzeni roboczej dla Twojego zespołu. Wyjątkowa trwałość i precyzyjne wykończenie sprawiają, że idealnie wpisuje się w standardy B2B. Zapewnij swojej firmie profesjonalny wizerunek na lata.",
        "{name} to synonim nowoczesnego podejścia do aranżacji biur i sal szkoleniowych. Solidna, stabilna konstrukcja sprosta najbardziej wymagającym warunkom użytkowania. Dbałość o ergonomię przekłada się na realny komfort pracy, podnosząc wydajność pracowników. Wybierz rozwiązanie cenione przez ekspertów z branży.",
        "Zapewnij swoim pracownikom i klientom najwyższy standard dzięki {name}. Produkt wyróżnia się wysoką odpornością na uszkodzenia mechaniczne, co jest kluczowe w intensywnie eksploatowanych przestrzeniach komercyjnych. Znakomicie łączy w sobie nowoczesny design z praktycznymi rozwiązaniami. Stanowi niezawodny element wyposażenia każdego profesjonalnego biura.",
        "Szukasz niezawodnego wyposażenia do przestrzeni komercyjnej? {name} oferuje bezkompromisową jakość wykonania i wieloletnią trwałość. Przemyślany, ergonomiczny kształt znacząco podnosi standard każdego stanowiska pracy. To inwestycja, która błyskawicznie zwraca się w postaci zwiększonego komfortu i wydajności."
    ],
    "Szafy i regały": [
        "Zoptymalizuj przestrzeń w swoim biurze z {name}. Ten pojemny i solidny mebel został zaprojektowany z myślą o maksymalnej funkcjonalności i trwałości. Wysokiej jakości materiały gwarantują odporność na codzienne użytkowanie w przestrzeniach B2B. Zachowaj porządek i profesjonalny wygląd swojego miejsca pracy.",
        "{name} to inteligentne rozwiązanie do przechowywania dokumentów i akcesoriów. Konstrukcja stworzona pod kątem intensywnej eksploatacji zapewnia wyjątkową stabilność i długowieczność. Ergonomiczne uchwyty i płynne mechanizmy ułatwiają codzienną pracę. Idealny wybór dla firm ceniących perfekcyjną organizację.",
        "Efektywne zarządzanie przestrzenią biurową wymaga odpowiednich narzędzi, a {name} sprawdzi się w tej roli doskonale. Solidne wykończenie i odporność na zarysowania czynią go idealnym wyborem dla obiektów komercyjnych. Zaprojektowany z dbałością o każdy detal, by służył bezawaryjnie przez wiele lat. Podnieś standard wyposażenia w swojej firmie.",
        "Uporządkowane biuro to podstawa efektywnej pracy. {name} pozwala na bezpieczne i ergonomiczne przechowywanie najważniejszych zasobów. Wykonany z wytrzymałych materiałów, doskonale odnajdzie się w biurach, szkołach i przestrzeniach komercyjnych. Profesjonalny wygląd idzie tu w parze z niezawodną jakością."
    ],
    "Elektronika i Edukacja": [
        "Wyposaż swoją firmę w innowacyjne rozwiązania, wybierając {name}. Sprzęt ten charakteryzuje się niezawodnością oraz doskonałymi parametrami technicznymi. Zoptymalizowany pod kątem ciągłej pracy, idealnie wpisuje się w rygorystyczne wymogi sektora B2B. Zwiększ efektywność swojego zespołu inwestując w sprawdzoną technologię.",
        "{name} to klucz do nowoczesnych szkoleń i dynamicznych prezentacji. Zapewnia wyjątkową jakość pracy, będąc stabilnym elementem wyposażenia sal konferencyjnych. Intuicyjna obsługa i długa żywotność komponentów minimalizują koszty utrzymania. To sprzęt, na którym profesjonaliści mogą polegać w każdej sytuacji.",
        "Inwestuj w technologię, która wspiera rozwój biznesu – wybierz {name}. Urządzenie zaprojektowano z myślą o maksymalnej wydajności i bezawaryjnej pracy w środowisku biznesowym. Jego ergonomia i zaawansowane funkcje znacząco usprawniają codzienne procesy. Gwarancja niezawodności potwierdzona zaufaniem wielu klientów korporacyjnych."
    ],
    "Tablice i akcesoria": [
        "Zwiększ efektywność spotkań biznesowych dzięki {name}. Odporna na zarysowania powierzchnia i solidny profil gwarantują niezmienną jakość przez lata. Produkt stworzony z myślą o salach konferencyjnych i placówkach edukacyjnych. Zapewnij prowadzącym narzędzie, które ułatwia klarowny przekaz i profesjonalną komunikację.",
        "{name} to niezbędne wsparcie dla każdej burzy mózgów i prezentacji. Stabilna, ergonomiczna konstrukcja zapewnia wygodę użytkowania nawet podczas wielogodzinnych warsztatów. Zastosowane materiały cechują się wyjątkową trwałością, idealną dla środowisk B2B. Wybierz jakość, która stymuluje kreatywność w zespole.",
        "Profesjonalne sale szkoleniowe wymagają niezawodnego sprzętu, a {name} spełnia te oczekiwania w stu procentach. Łatwość czyszczenia i odporność na intensywną eksploatację to jego największe atuty. Doskonale sprawdzi się w biurach, hotelach i centrach edukacyjnych. Solidność wykonania podnosi prestiż każdego spotkania."
    ],
    "Krzesła i fotele": [
        "Ergonomia to klucz do sukcesu, dlatego {name} został zaprojektowany z myślą o najwyższym komforcie. Solidna podstawa i trwałe materiały obiciowe idealnie sprawdzą się w intensywnie użytkowanych biurach i przestrzeniach HoReCa. Gwarantuje prawidłowe wsparcie sylwetki przez cały dzień pracy. Zadbaj o zdrowie i wydajność swoich pracowników.",
        "Odkryj nowy wymiar profesjonalizmu z {name}. Ten model łączy w sobie nowoczesny design z ponadprzeciętną wytrzymałością konstrukcyjną. Idealny do sal konferencyjnych, hoteli oraz ekskluzywnych przestrzeni biurowych. Zapewnia doskonałą ergonomię, stanowiąc niezawodną inwestycję dla każdej firmy.",
        "{name} to odpowiedź na potrzeby nowoczesnych przestrzeni komercyjnych. Zastosowanie wysokiej jakości tkanin i wzmocnionej ramy zapewnia wyjątkową trwałość, nawet przy dużym obciążeniu. Profilowane oparcie i precyzyjna regulacja wspierają zdrową pozycję podczas pracy. To wyposażenie, które buduje zaufanie i profesjonalny wizerunek.",
        "Komfort spotyka się z wytrzymałością w modelu {name}. Przeznaczony do rygorystycznych warunków sektora B2B, gwarantuje bezproblemowe użytkowanie przez długie lata. Ergonomiczne ukształtowanie zapobiega zmęczeniu, podnosząc komfort wielogodzinnych sesji. Niezbędny element wyposażenia dla placówek edukacyjnych i firm."
    ],
    "Place Zabaw": [
        "Zapewnij najwyższy standard bezpieczeństwa z {name}. Ten certyfikowany produkt wykonano z wyjątkowo trwałych materiałów, odpornych na warunki atmosferyczne i intensywną eksploatację. Idealny wybór dla ośrodków wypoczynkowych, hoteli i przedszkoli ceniących solidność. Ergonomiczna konstrukcja wspiera rozwój w bezpiecznym otoczeniu.",
        "{name} to synonim bezpiecznej i rozwijającej zabawy. Trwała konstrukcja gwarantuje niezawodność, co jest kluczowe w przestrzeniach publicznych i obiektach komercyjnych. Odpowiednio wyprofilowane elementy zapewniają pełną ergonomię i minimalizują ryzyko urazów. Inwestycja w jakość, która przyciągnie rodziny z dziećmi do Twojego obiektu.",
        "Solidność i estetyka to główne cechy {name}. Zaprojektowany z uwzględnieniem rygorystycznych norm jakościowych, idealnie sprawdzi się na terenie pensjonatów i restauracji. Gwarantuje wieloletnią odporność i atrakcyjny wygląd pomimo upływu czasu. Stwórz przestrzeń przyjazną najmłodszym bez kompromisów w kwestii trwałości."
    ]
}

generic_templates = [
    "{name} to produkt spełniający najwyższe standardy branży B2B i HoReCa. Oferuje niezrównaną trwałość oraz solidne wykonanie, które zadowoli najbardziej wymagających profesjonalistów. Ergonomiczny kształt i dbałość o detale znacząco podnoszą komfort użytkowania na co dzień. Stanowi pewną inwestję na lata w rozwój Twojego biznesu.",
    "Zmodernizuj swoją przestrzeń dzięki {name}, produktowi stworzonemu dla sektora biznesowego. Niezawodna jakość wykonania gwarantuje wytrzymałość nawet przy najintensywniejszej eksploatacji. Starannie przemyślana ergonomia ułatwia codzienną obsługę i podnosi standard obiektu. Wybierz rozwiązanie polecane przez ekspertów komercyjnych."
]

random.seed(1234)

for product in data.get('products', []):
    category = product.get('category', '')
    name = product.get('name', 'Ten produkt')
    
    pool = templates.get(category, generic_templates)
    chosen_template = random.choice(pool)
    new_desc = chosen_template.format(name=name)
    
    product['description'] = new_desc

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Pomyślnie zaktualizowano opisy wszystkich produktów.")