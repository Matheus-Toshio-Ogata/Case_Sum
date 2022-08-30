# Task 3

## Django
- Your next goal is to implement a `POST` method for inserting trading blotters into your database.
- Don't forget to read the recommended links.

## React
- Implement a way to create a new trade blotter.
  - We prefer that new items are inserted directly in the table and then saved to the database by some action, but this is not mandatory. You can implement it in any way you wish.

> _If you want to be more compatible with our current solution, use Material UI and React Table._

### Example:

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
        <td></td>
    </tr>
    <tr>
        <td>VALE3</td>
        <td>100</td>
        <td>27.6</td>
        <td>John</td>
        <td>John@bank1</td>
        <td></td>
    </tr>
    <tr>
        <td>VALE3</td>
        <td>200</td>
        <td>26.3</td>
        <td>John</td>
        <td>John@bank1</td>
        <td></td>
    </tr>
    <tr>
        <td>VALE3</td>
        <td>300</td>
        <td>26</td>
        <td>John</td>
        <td>John@bank1</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="width:10px;">+</td>
    </tr>
</table>
If you click to add (+) a new row...
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
        <td></td>
    </tr>
    <tr>
        <td>VALE3</td>
        <td>100</td>
        <td>27.6</td>
        <td>John</td>
        <td>John@bank1</td>
        <td></td>
    </tr>
    <tr>
        <td>VALE3</td>
        <td>200</td>
        <td>26.3</td>
        <td>John</td>
        <td>John@bank1</td>
        <td></td>
    </tr>
    <tr>
        <td>VALE3</td>
        <td>300</td>
        <td>26</td>
        <td>John</td>
        <td>John@bank1</td>
        <td></td>
    </tr>
    <tr>
        <td style="background-color:#36a1364d;">PETR4 </td>
        <td style="background-color:#36a1364d;">100</td>
        <td style="background-color:#36a1364d;">27</td>
        <td style="background-color:#36a1364d;">Me</td>
        <td style="background-color:#36a1364d;">Me@bank2</td>
        <td style="background-color:#36a1364d;">SEND</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td style="width:10px;">+</td>
    </tr>
</table>
