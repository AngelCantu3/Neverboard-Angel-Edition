<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebsiteStart.aspx.cs" Inherits="NeverBoard.WebForm1" %>
<!--MARIE created a normal asp.net web application (.net framwork) with https configuration-->
<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">

<head runat="server">
    <script src="MapJS.js"></script>
    <link href= "MapCSS.css" rel="stylesheet" /> <!--CSS file for the website linked here-->
    <title>Senior Project Google Map</title>

     

</head>
<body>
    <form id="form1" runat="server">
    <h1>Never Board</h1>




            <div>
            <!--Left side div-->
            <div id="map" style="width: 73%; float: left;">

            </div>

            <!--Right side div-->
            <div>
                <asp:TextBox ID="txtInfoPanel" runat="server" CssClass="infoPanel" TextMode="MultiLine" Width="23%"></asp:TextBox>
            </div>
        </div>


    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDAGqUMbz0cdb-U5HSTFBKH1S4o2ucfg38&callback=initMap">
    </script>

    </form>

</body>
</html>
