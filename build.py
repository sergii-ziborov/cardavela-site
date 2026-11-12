#!/usr/bin/env python3
"""Builds the static Cardavela site: landing, privacy, terms and support in English and Russian."""
import json, pathlib
BASE = "https://sergii-ziborov.github.io/cardavela-site/"
STORE = "https://apps.apple.com/app/id6825797949"
ISSUES = "https://github.com/sergii-ziborov/cardavela-site/issues"
UPDATED = "2026-11-12"
root = pathlib.Path(__file__).parent

L = {
"en": dict(
  lang="en", prefix="", other="ru/", other_name="Русский",
  nav=("Features","Privacy","Terms","Support"),
  title="Cardavela — English & Russian flashcards with swipes, charts and free word decks",
  desc="Learn English and Russian words with flip cards: swipe right if you know it, left if you don't. Free decks of the most frequent words and phrases, spaced repetition, colorful statistics and your own decks. Works offline, no account.",
  kw="flashcards, learn English, learn Russian, vocabulary, spaced repetition, Anki import, word cards, English words, Russian words, language learning app",
  h1="Learn words with a swipe.",
  lead="One card fills the screen. Tap to flip. Swipe right — you know it. Swipe left — it comes back sooner. Cardavela turns English and Russian vocabulary into short, colorful sessions.",
  cta="Download on the App Store", badges=("Free decks","Works offline","No account","Spaced repetition"),
  feat_h="Why Cardavela",
  feats=[("#0C5C59","↺","Flip and swipe","A 3D flip shows the answer with an example and native speech. Know / Hard / Don't know — three buttons or one swipe."),
         ("#E5484D","✕","Know and don't know lists","Every word lands in Don't know, Hard or Know. Train only the words you don't know, or play Pairs and Ring with them."),
         ("#7B5CF0","▮","Colorful statistics","Streaks, marks per day, words by list, returns for the week ahead and a 12-week study calendar."),
         ("#23A26D","★","Free word decks","Frequent English words and phrases from films and series with Russian meanings — over 39,000 pairs in both directions. A deck store with more decks is coming."),
         ("#1AA7C9","⇩","Your own decks","Type a card, import an Anki .apkg, or a simple TXT/CSV list: word — translation. Share your deck as one file."),
         ("#E8930C","⏱","Spaced repetition","FSRS scheduling brings each card back right before you'd forget it. Sessions are short: up to 8 cards."),
         ("#E5484D","⌚","Apple Watch","Study cards on your wrist with Know and Don't know. Answers sync to your iPhone automatically.")],
  shots_h="Screens", faq_h="Questions",
  faq=[("Is Cardavela free?","Yes. The app and all current decks are free. Paid decks may appear in the in-app deck store later; free decks stay free."),
       ("Do I need an account?","No. Your cards and answers stay on your device. You can export a personal backup file."),
       ("Which languages?","Cards are English ↔ Russian in both directions. The interface is in Russian, English, Hebrew, Spanish and Arabic."),
       ("Can I import my Anki deck?","Yes: legacy .apkg packages and plain TXT/CSV/TSV word lists. The schedule is not copied: Cardavela starts memory fresh."),
       ("Is the meaning checked?","The published pairs come from a frequency count of film and series subtitles. They are not a checked dictionary; the app marks this on the card.")],
  footer="© 2026 Cardavela. Made for short daily practice.",
),
"ru": dict(
  lang="ru", prefix="../", other="../", other_name="English",
  nav=("Возможности","Конфиденциальность","Условия","Поддержка"),
  title="Cardavela — карточки английских и русских слов: свайпы, графики и бесплатные колоды",
  desc="Учите английские и русские слова карточками: свайп вправо — знаю, влево — не знаю. Бесплатные колоды частых слов и фраз, интервальные повторения, яркая статистика и свои колоды. Без интернета и без регистрации.",
  kw="карточки, учить английский, английские слова, русские слова, словарный запас, интервальное повторение, флеш-карточки, Anki, приложение для изучения слов",
  h1="Учите слова свайпом.",
  lead="Одна карточка на весь экран. Нажмите — перевернётся. Свайп вправо — знаю. Свайп влево — вернётся раньше. Cardavela превращает английские и русские слова в короткие яркие занятия.",
  cta="Скачать в App Store", badges=("Бесплатные колоды","Работает без сети","Без регистрации","Интервальные повторения"),
  feat_h="Почему Cardavela",
  feats=[("#0C5C59","↺","Переворот и свайпы","Объёмный переворот показывает ответ с примером и озвучкой. «Знаю / Сложно / Не знаю» — три кнопки или один свайп."),
         ("#E5484D","✕","Списки «знаю» и «не знаю»","Каждое слово попадает в «Не знаю», «Сложно» или «Знаю». Учите только незнакомые слова или играйте с ними в «Пары» и «Кольцо»."),
         ("#7B5CF0","▮","Яркая статистика","Дни подряд, ответы по дням, слова по спискам, повторения на неделю вперёд и календарь за 12 недель."),
         ("#23A26D","★","Бесплатные колоды","Частые английские слова и фразы из фильмов и сериалов с русскими значениями — больше 39 000 пар в обе стороны. Скоро — магазин новых колод."),
         ("#1AA7C9","⇩","Свои колоды","Наберите карточку, импортируйте Anki .apkg или простой список TXT/CSV: слово — перевод. Делитесь колодой одним файлом."),
         ("#E8930C","⏱","Интервальные повторения","Расписание FSRS возвращает карточку как раз перед тем, как вы её забудете. Занятия короткие: до 8 карточек."),
         ("#E5484D","⌚","Apple Watch","Учите карточки на часах: «Знаю» и «Не знаю». Ответы сами попадают на iPhone.")],
  shots_h="Экраны", faq_h="Вопросы",
  faq=[("Cardavela бесплатная?","Да. Приложение и все нынешние колоды бесплатны. Позже в магазине колод могут появиться платные наборы; бесплатные останутся бесплатными."),
       ("Нужна ли регистрация?","Нет. Карточки и ответы хранятся на вашем устройстве. Можно сохранить личную копию в файл."),
       ("Какие языки?","Карточки английский ↔ русский в обе стороны. Интерфейс: русский, английский, иврит, испанский и арабский."),
       ("Можно импортировать колоду Anki?","Да: пакеты .apkg и простые списки TXT/CSV/TSV. Расписание не копируется — память начинается заново."),
       ("Значения проверены?","Опубликованные пары — подсчёт по субтитрам фильмов и сериалов, а не проверенный словарь. Приложение помечает это на карточке.")],
  footer="© 2026 Cardavela. Для коротких ежедневных занятий.",
),
}

PRIVACY = {
"en": ("Privacy Policy", f"""<p class="muted">Last updated: {UPDATED}</p>
<p>Cardavela is a flashcard app. This policy explains what data the app handles. In short: <b>your cards and answers stay on your device, the app has no account, no ads and no tracking.</b></p>
<h2>Data stored on your device</h2><p>Your decks, cards you type or import, your answers (self-assessments), schedules and settings are saved only in the app's storage on your device. They are not sent to us. iOS may include them in your device backup (iCloud or computer) under your own Apple settings.</p>
<h2>Downloading decks</h2><p>When you download a deck, the app requests the deck file from our server over HTTPS. Like any web server, it receives your IP address and the standard request headers in its access logs for security and abuse protection. Logs are not linked to an identity, are not used for advertising and are deleted on rotation (typically within 30 days). No account, device identifier or answer data is sent.</p>
<h2>Links and imported files</h2><p>If you open a deck from a link, the app downloads that file from the address you entered. Files you import are read on your device only.</p>
<h2>Speech</h2><p>Pronunciation uses the voices built into iOS on your device. Cardavela does not record or upload audio.</p>
<h2>Analytics, ads and tracking</h2><p>Cardavela contains no third-party analytics, advertising or tracking SDKs and does not track you across apps or websites.</p>
<h2>Backups you export</h2><p>A personal backup is a file you create and keep. It contains your decks and answers. Share it only with people you trust.</p>
<h2>Children</h2><p>The app does not knowingly collect personal data from anyone, including children.</p>
<h2>Purchases</h2><p>The app is free today. If paid decks appear later, payments are processed by Apple; we receive no payment card details.</p>
<h2>Your choices</h2><p>Delete a deck in the Library or delete the app to remove all data stored by Cardavela on your device.</p>
<h2>Changes and contact</h2><p>We will update this page when the app changes how it handles data. Questions: <a href="{ISSUES}">contact support</a>.</p>"""),
"ru": ("Политика конфиденциальности", f"""<p class="muted">Обновлено: {UPDATED}</p>
<p>Cardavela — приложение с карточками. Здесь сказано, какие данные оно обрабатывает. Коротко: <b>ваши карточки и ответы остаются на устройстве, учётной записи, рекламы и отслеживания нет.</b></p>
<h2>Данные на устройстве</h2><p>Колоды, карточки, которые вы набрали или импортировали, ваши ответы (самооценки), расписание и настройки хранятся только в хранилище приложения на вашем устройстве и нам не передаются. iOS может включать их в резервную копию устройства (iCloud или компьютер) по вашим настройкам Apple.</p>
<h2>Скачивание колод</h2><p>При скачивании колоды приложение запрашивает файл с нашего сервера по HTTPS. Как любой веб-сервер, он получает ваш IP-адрес и стандартные заголовки запроса в журналах доступа для безопасности и защиты от злоупотреблений. Журналы не связываются с личностью, не используются для рекламы и удаляются при ротации (обычно в течение 30 дней). Учётная запись, идентификатор устройства и ваши ответы не передаются.</p>
<h2>Ссылки и импортированные файлы</h2><p>Если вы открываете колоду по ссылке, приложение скачивает файл по указанному вами адресу. Импортированные файлы читаются только на устройстве.</p>
<h2>Озвучка</h2><p>Произношение использует встроенные голоса iOS на устройстве. Cardavela не записывает и не отправляет звук.</p>
<h2>Аналитика, реклама и отслеживание</h2><p>В Cardavela нет сторонней аналитики, рекламы и SDK отслеживания; приложение не отслеживает вас в других приложениях и на сайтах.</p>
<h2>Личные копии</h2><p>Личная копия — файл, который вы создаёте и храните сами. В нём ваши колоды и ответы. Передавайте его только тем, кому доверяете.</p>
<h2>Дети</h2><p>Приложение сознательно не собирает персональные данные ни у кого, в том числе у детей.</p>
<h2>Покупки</h2><p>Сейчас приложение бесплатное. Если позже появятся платные колоды, оплату обрабатывает Apple; данные карты нам не передаются.</p>
<h2>Ваш выбор</h2><p>Удалите колоду в «Библиотеке» или удалите приложение, чтобы стереть все данные Cardavela на устройстве.</p>
<h2>Изменения и связь</h2><p>Мы обновим эту страницу, если приложение изменит обработку данных. Вопросы: <a href="{ISSUES}">служба поддержки</a>.</p>"""),
}
TERMS = {
"en": ("Terms of Use", f"""<p class="muted">Last updated: {UPDATED}</p>
<p>These terms govern your use of the Cardavela app and website. By using Cardavela you agree to them. If you download the app from the App Store, Apple's <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Standard Licensed Application End User License Agreement</a> also applies; where these terms differ, the Apple EULA prevails for the app license.</p>
<h2>1. The license</h2><p>We grant you a personal, non-exclusive, non-transferable license to use Cardavela on Apple devices you own or control, for personal, non-commercial learning.</p>
<h2>2. Learning content</h2><p>Published decks are built from frequency counts of film and series subtitles. They are provided for study and are not a verified dictionary; meanings and examples may be incomplete or inaccurate. Self-assessment marks are your own judgment and are not checked answers.</p>
<h2>3. Your content</h2><p>You are responsible for the cards, decks and files you create, import or share, and you must have the right to use them. Do not import or share material that infringes others' rights or is unlawful.</p>
<h2>4. Deck store and purchases</h2><p>All current decks are free. If paid decks are offered later, prices are shown before purchase and payments, refunds and family sharing are handled by Apple under its terms. Free decks will remain free.</p>
<h2>5. Acceptable use</h2><p>Do not attempt to disrupt our servers, bypass integrity checks, scrape or redistribute published decks in bulk, or reverse engineer the app except where the law allows.</p>
<h2>6. Availability</h2><p>We may change, add or remove features and decks. We aim to keep downloaded decks usable offline, but we do not guarantee uninterrupted service.</p>
<h2>7. No warranty</h2><p>Cardavela is provided "as is" without warranties of any kind, to the extent permitted by law.</p>
<h2>8. Limitation of liability</h2><p>To the extent permitted by law, we are not liable for indirect or consequential damages, or for loss of data. Keep a personal backup of important decks.</p>
<h2>9. Changes</h2><p>We may update these terms; the date above shows the latest version. Continued use means you accept the updated terms.</p>
<h2>10. Contact</h2><p><a href="{ISSUES}">Contact support</a>.</p>"""),
"ru": ("Условия использования", f"""<p class="muted">Обновлено: {UPDATED}</p>
<p>Эти условия регулируют использование приложения и сайта Cardavela. Пользуясь Cardavela, вы их принимаете. Если приложение скачано из App Store, действует также <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">Стандартное лицензионное соглашение Apple (EULA)</a>; при расхождении для лицензии на приложение приоритет у EULA Apple.</p>
<h2>1. Лицензия</h2><p>Мы предоставляем вам личную, неисключительную, непередаваемую лицензию на использование Cardavela на ваших устройствах Apple для личного некоммерческого обучения.</p>
<h2>2. Учебные материалы</h2><p>Опубликованные колоды построены на подсчёте частотности субтитров фильмов и сериалов. Они предназначены для учёбы и не являются проверенным словарём; значения и примеры могут быть неполными или неточными. Отметки самооценки — ваше собственное решение, а не проверенный ответ.</p>
<h2>3. Ваши материалы</h2><p>Вы отвечаете за карточки, колоды и файлы, которые создаёте, импортируете или передаёте, и должны иметь право их использовать. Не импортируйте и не распространяйте материалы, нарушающие права других или закон.</p>
<h2>4. Магазин колод и покупки</h2><p>Все нынешние колоды бесплатны. Если позже появятся платные колоды, цена будет показана до покупки, а оплату, возвраты и семейный доступ обрабатывает Apple по своим правилам. Бесплатные колоды останутся бесплатными.</p>
<h2>5. Допустимое использование</h2><p>Не пытайтесь нарушить работу серверов, обойти проверки целостности, массово выгружать или распространять опубликованные колоды и не декомпилируйте приложение, кроме случаев, разрешённых законом.</p>
<h2>6. Доступность</h2><p>Мы можем менять, добавлять и убирать функции и колоды. Скачанные колоды стараемся сохранять доступными без сети, но не гарантируем бесперебойную работу.</p>
<h2>7. Отказ от гарантий</h2><p>Cardavela предоставляется «как есть», без каких-либо гарантий в пределах, допустимых законом.</p>
<h2>8. Ограничение ответственности</h2><p>В пределах, допустимых законом, мы не отвечаем за косвенные убытки и потерю данных. Храните личную копию важных колод.</p>
<h2>9. Изменения</h2><p>Мы можем обновлять условия; дата выше показывает последнюю версию. Продолжая пользоваться приложением, вы принимаете обновлённые условия.</p>
<h2>10. Связь</h2><p><a href="{ISSUES}">Служба поддержки</a>.</p>"""),
}
SUPPORT = {
"en": ("Support", f"""<p>Need help with Cardavela? Open a request on our <a href="{ISSUES}">support page</a> — describe the problem, your iPhone/iPad model and iOS version. We usually reply within 2 business days.</p>
<h2>Quick answers</h2>
<details><summary>How do I study?</summary><p>Open My cards and tap the start button, or start any deck in the Library. Tap the card to flip it, then swipe right (Know), left (Don't know) or up (Easy), or use the three buttons.</p></details>
<details><summary>How do I download or delete a deck?</summary><p>Library → Deck store → Download. To delete, tap “…” on a deck in My decks. Your answers stay in statistics.</p></details>
<details><summary>How do I import my words?</summary><p>Library → “+” → Import a deck. Choose an Anki .apkg or a TXT/CSV list with one pair per line: word, tab or “;” or “ - ”, translation.</p></details>
<details><summary>How do I move to a new phone?</summary><p>Settings → Backup → Export backup, then Restore backup on the new device. A normal iPhone backup also keeps the app data.</p></details>
<details><summary>A word is not spoken</summary><p>Install an English or Russian voice in iOS Settings → Accessibility → Spoken Content → Voices.</p></details>"""),
"ru": ("Поддержка", f"""<p>Нужна помощь с Cardavela? Оставьте запрос на <a href="{ISSUES}">странице поддержки</a> — опишите проблему, модель iPhone/iPad и версию iOS. Обычно отвечаем в течение 2 рабочих дней.</p>
<h2>Быстрые ответы</h2>
<details><summary>Как заниматься?</summary><p>Откройте «Мои карточки» и нажмите кнопку занятия или начните любую колоду в «Библиотеке». Нажмите на карточку, чтобы перевернуть, затем свайп вправо («Знаю»), влево («Не знаю») или вверх («Легко») — или три кнопки внизу.</p></details>
<details><summary>Как скачать или удалить колоду?</summary><p>«Библиотека» → «Магазин колод» → «Скачать». Чтобы удалить, нажмите «…» на колоде в «Моих колодах». Ответы останутся в статистике.</p></details>
<details><summary>Как импортировать свои слова?</summary><p>«Библиотека» → «+» → «Импорт колоды». Выберите Anki .apkg или список TXT/CSV, одна пара на строку: слово, табуляция, «;» или « - », перевод.</p></details>
<details><summary>Как перенести на новый телефон?</summary><p>«Настройки» → «Личная копия» → «Экспорт», затем «Восстановить» на новом устройстве. Обычная резервная копия iPhone тоже сохраняет данные приложения.</p></details>
<details><summary>Слово не озвучивается</summary><p>Установите английский или русский голос: «Настройки» iOS → «Универсальный доступ» → «Устная речь» → «Голоса».</p></details>"""),
}

def page(l, path, title, desc, body, kind="page"):
    c = L[l]; p = c["prefix"]
    alt_path = path
    en_url = BASE + path; ru_url = BASE + "ru/" + path
    ld = {"@context":"https://schema.org","@type":"MobileApplication","name":"Cardavela","operatingSystem":"iOS 17+","applicationCategory":"EducationalApplication","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"description":c["desc"],"inLanguage":l,"url":BASE if l=="en" else BASE+"ru/","installUrl":STORE,"image":BASE+"assets/icon.png"}
    other_href = (("ru/" + path) if l=="en" else ("../" + path)) or ("ru/" if l=="en" else "../")
    return f"""<!doctype html><html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta name="keywords" content="{c['kw']}">
<link rel="canonical" href="{en_url if l=='en' else ru_url}"><link rel="alternate" hreflang="en" href="{en_url}"><link rel="alternate" hreflang="ru" href="{ru_url}"><link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{BASE}assets/og.png"><meta property="og:url" content="{en_url if l=='en' else ru_url}"><meta name="twitter:card" content="summary_large_image">
<meta name="apple-itunes-app" content="app-id=6825797949"><link rel="icon" href="{p}assets/icon.png"><link rel="apple-touch-icon" href="{p}assets/icon.png"><link rel="stylesheet" href="{p}assets/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script></head><body><div class="wrap">
<header class="top"><a class="brand" href="{'./' if l=='en' else './'}{'' }index.html"><img src="{p}assets/icon.png" alt="">Cardavela</a>
<nav><a href="index.html#features">{c['nav'][0]}</a><a href="privacy.html">{c['nav'][1]}</a><a href="terms.html">{c['nav'][2]}</a><a href="support.html">{c['nav'][3]}</a><a href="{other_href}" hreflang="{'ru' if l=='en' else 'en'}">{c['other_name']}</a></nav></header>
{body}
<footer>{c['footer']}<br><a href="privacy.html">{c['nav'][1]}</a><a href="terms.html">{c['nav'][2]}</a><a href="support.html">{c['nav'][3]}</a><a href="{STORE}">App Store</a></footer></div></body></html>"""

def landing(l):
    c = L[l]; p = c["prefix"]
    feats = "".join(f'<div class="card"><div class="ico" style="background:{col}">{ic}</div><h3>{h}</h3><p>{t}</p></div>' for col,ic,h,t in c["feats"])
    shots = "".join(f'<img src="{p}assets/shot-{i}-{l}.png" alt="Cardavela screen {i}" loading="lazy">' for i in range(1,6))
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in c["faq"])
    fq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in c["faq"]]}
    body = f"""<section class="hero"><div><h1>{c['h1']}</h1><p>{c['lead']}</p><a class="cta" href="{STORE}"> {c['cta']}</a>
<div class="badges">{''.join(f'<span class="badge">{b}</span>' for b in c['badges'])}</div></div><img class="shot" src="{p}assets/shot-1-{l}.png" alt="Cardavela"></section>
<h2 id="features">{c['feat_h']}</h2><div class="grid">{feats}</div>
<h2>{c['shots_h']}</h2><div class="shots">{shots}</div>
<h2>{c['faq_h']}</h2>{faq}<script type="application/ld+json">{json.dumps(fq, ensure_ascii=False)}</script>"""
    return page(l, "index.html", c["title"], c["desc"], body)

for l in ("en","ru"):
    out = root if l=="en" else root/"ru"
    (out/"index.html").write_text(landing(l), encoding="utf-8")
    for name, data in (("privacy",PRIVACY),("terms",TERMS),("support",SUPPORT)):
        t, html = data[l]
        (out/f"{name}.html").write_text(page(l, f"{name}.html", f"{t} — Cardavela", L[l]["desc"][:150], f'<article class="doc"><h1>{t}</h1>{html}</article>'), encoding="utf-8")
urls = [BASE+p for p in ("","privacy.html","terms.html","support.html")] + [BASE+"ru/"+p for p in ("","privacy.html","terms.html","support.html")]
(root/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{u}</loc><lastmod>{UPDATED}</lastmod></url>" for u in urls)+"</urlset>\n")
(root/"robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n")
(root/".nojekyll").write_text("")
print("built")
