<%@ page contentType="text/html;charset=UTF-8" %>
<%@ page import="data.Result" %>
<%@ page import="data.ResultList" %>
<%@ page import="java.util.Arrays" %>
<%@ page import="java.util.ArrayList" %>

<html lang="en">

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
    <title>Web Lab #2</title>
</head>

<body>
<table id="main-grid">
    <tr>
        <!-- Header -->
        <td id="header-plate" colspan="2">
            <span class="left-aligned">Владимир Мацюк, P3215</span>
            <span class="right-aligned">№666</span>
        </td>
        <td>
        </td>
    </tr>

    <tr>
        <!-- Graph -->
        <td class="content-plate" id="graph-plate" rowspan="2">
            <div class="plate-top">
                <h2 class="plate-top-title">Граф</h2>
            </div>

            <div class="image-container">
<%--                <img src="assets/graph.svg" width="640" height="640">--%>
    <canvas id="plot" width="300" height="300"></canvas>
            </div>
        </td>
        <!-- Table -->
        <td class="content-plate table-view" id="table-plate">
            <div class="plate-top">
                <%=(request.getAttribute("errorMessage") != null)
                        ?
                        ("<h2 id =\"error-Table\" class=\"miss-text plate-top\">Таблица -> "+request.getAttribute("errorMessage")+"</h2>")
                        :
                        "<h2 id =\"error-Table\" class=\"plate-top-title\">Таблица</h2>"
                %>
            </div>

            <div class="scroll-container">
                <table id="result-table">
                    <thead>
                    <tr class="table-header">
                        <th class="coords-col">X</th>
                        <th class="coords-col">Y</th>
                        <th class="coords-col">R</th>
                        <th class="time-col">Время</th>
                        <th class="time-col">Время исполнения</th>
                        <th class="hitres-col">Результат</th>
                    </tr>
                    </thead>
                    <tbody>
                    <%
                        ResultList resultList;
                        if (session.getAttribute("results") == null) {
                            resultList = new ResultList();
                        } else {
                            resultList = (ResultList) session.getAttribute("results");
                        }

                        for (Result result : resultList) {
                    %>
                    <tr>
                        <td class="table-text"><%=result.getX()%></td>
                        <td class="table-text"><%=result.getY()%></td>
                        <td class="table-text"><%=result.getR()%></td>
                        <td class="table-text"><%=result.getCurrTime()%></td>
                        <td class="table-text"><%=result.getExecTime()%></td>
                        <td class="table-text"><%=result.isHitResult() ? "✅" : "❌"%></td>
                        
                    </tr>
                    <% } %>
                    </tbody>
                </table>
            </div>
        </td>
    </tr>

    <tr>
        <!-- Values -->
        <td class="content-plate values-view" id="values-plate">
            <div class="plate-top">
                <h2 class="plate-top-title">Values</h2>
            </div>

            <form id="input-form">
                <table id="input-grid">
                    <!-- X Values -->
                    <tr>
                        <td class="input-grid-label">
                            <label for="x-textinput">X:</label>
                        </td>

                        <td class="input-grid-value">
                            <input id="x-textinput" type="text" name="x" maxlength="10" autocomplete="off"
                                   placeholder="-3 ... 3" value="<%=(resultList.getSize() <= 0) ? "" : resultList.getResult(resultList.getSize() - 1).getX()%>">
                        </td>
                    </tr>

                    <!-- Y Values -->

                    <tr>
                        <td class="input-grid-label">
                            <label>Y:</label>
                        </td>
                        <td class="input-grid-value">
                            <div required name="y" id="y">

                                    <%
                        ArrayList<Double> list = new ArrayList<>(Arrays.asList(-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0,4.0,5.0));

                        for (Double value : list) {
                    %>
                                <input type="checkbox"
                                name="y" 
                                        value="<%=value%>"
                                        <%=(resultList.getSize() > 0 && (resultList.getResult(resultList.getSize() - 1)).getY()==value) ? "selected" : ""%>>
                                </input>
                                <label class="rbox-label" for="y-checkbox"><%=value%></label>

                    <% } %>
                            </select>
                        </td>
                    </tr>

                    <!-- R Values -->
                    <tr>
                        <td class="input-grid-label">
                            <label>R:</label>
                        </td>
                        <td class="input-grid-value r-radio-group">

                            <%
                                ArrayList<Double> rList = new ArrayList<>(Arrays.asList(1.0,1.5,2.0,2.5,3.0));

                                for (int i = 0; i < rList.size(); i++) {
                            %>

                            <div class="center-labeled">
                                <label class="rbox-label" for="r-radio<%=i+1%>"><%=rList.get(i)%></label>
                                <input class="r-radio" id="r-radio<%=i+1%>" type="radio" name="r" value=<%=rList.get(i)%> <%=(resultList.getSize() > 0 && (resultList.getResult(resultList.getSize() - 1)).getR()==rList.get(i)) ? "checked" : ""%>>
                            </div>
                            <% } %>
                        </td>
                    </tr>

                    <!-- Buttons -->
                    <tr>
                        <td colspan="2">
                            <div class="buttons">
                                <input id="submitBtn" class="button" type="submit" value="Ввести">
                                <input id="resetBtn" class="button" type="reset" value="Сброс">
                            </div>
                        </td>
                    </tr>
                </table>
            </form>
        </td>
    </tr>
</table>

<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<script type='text/javascript' src="js/main.js"></script>
<script type='text/javascript' src="js/graph.js"></script>
<script type="text/javascript">
    $(document).ready(drawGraph());
</script>
</body>

</html>