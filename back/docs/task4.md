# Task 4

## Django
- In this step, you should implement a service in any language that will check a list of trading blotters on a text file and send them to your "create new blotter" (POST) endpoint.
- This text file will be generated automatically by `blotter_generator.py`, so you should keep it running while your service runs.
- There are no restrictions on how you should implement your service, but you should aim to reduce the delay between the time the information was generated and the time it was inserted on your database.
> _Hint: you probably want to make a request only when the file was changed_

## React
- Your table should now request blotters more often (30-second interval).
- Enable and disable value aggregation by ticker, with average price given by the weighted average.
- Your styling will be noted.

### Example

**Detailed**
<table>
    <tr>
        <td><b>ticker</b></td>
        <td><b>volume</b></td>
        <td><b>price</b></td>
        <td><b>user_name</b></td>
        <td><b>user_email</b></td>
        <td style="border:0px; width:10px;"></td>
    </tr>
    <tr>
        <td>VALE3</td>
        <td>100</td>
        <td>27.5</td>
        <td>John</td>
        <td>John@bank1</td>
    </tr>
    <tr>
        <td>VALE3</td>
        <td>100</td>
        <td>27.6</td>
        <td>John</td>
        <td>John@bank1</td>
    </tr>
    <tr>
        <td>VALE3</td>
        <td>200</td>
        <td>26.3</td>
        <td>John</td>
        <td>John@bank1</td>
    </tr>
    <tr>
        <td>VALE3</td>
        <td>300</td>
        <td>26</td>
        <td>John</td>
        <td>John@bank1</td>
    </tr>
    <tr>
        <td style="border:0px"></td>
        <td style="border:0px"></td>
        <td style="border:0px"></td>
        <td style="border:0px"></td>
        <td style="border:0px"></td>
        <td style="border:0px;width:10px;">+</td>
    </tr>
</table>

**Aggregated**
<table>
    <tr>
        <td><b>ticker</b></td>
        <td><b>volume</b></td>
        <td><b>price</b></td>
        <td><b>user_name</b></td>
        <td><b>user_email</b></td>
        <td style="border:0px; width:10px;"></td>
    </tr>
    <tr>
        <td>VALE3</td>
        <td>700</td>
        <td>26.53</td>
        <td>John</td>
        <td>John@bank1</td>
    </tr>
    <tr>
        <td style="border:0px"></td>
        <td style="border:0px"></td>
        <td style="border:0px"></td>
        <td style="border:0px"></td>
        <td style="border:0px"></td>
        <td style="border:0px;width:10px;">+</td>
    </tr>
</table>