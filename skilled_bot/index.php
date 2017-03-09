<DOCTYPE! html>
    <html>

    <head>
        <script type="text/javascript" src="reddit.js"></script>
        <link rel="stylesheet" type="text/css" href="style.css">

    </head>

    <body>
        <div class="header">
            <h1>SKILLED AF</h1>
            <div class="nav">
                <a href="#">About</a>
                <a href="#">Sugjestions</a>
                <a href="#">Donate</a>
            </div>
        </div>
        <div class="filter">
            <div>Gaming:<input id="box1" checked class="selection" data-cls="gaming" type="checkbox"></div>
            <br/>
            <div>ModernMagic:<input id="box2" checked class="selection" data-cls="modernmagic" type="checkbox"></div>
            <br/>
            <div>Sports:<input id="box3" checked class="selection" data-cls="sports" type="checkbox"></div>
            <br/>

        </div>
        <div class="wrapper">
            <!--reddit link-->
            <?php include 'links.php'?>
        </div>
    </body>

    </html>
