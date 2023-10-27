let count = 1;
let elc = 2;
 
function addRow()
{const table = document.getElementById("mainTable");
const newRow = table.insertRow(++count);



    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    cell1.innerHTML =  `<input type="number" name="x_axis"/>`;
    cell2.innerHTML =  `<input type="number" name="y_axis"/>`;

    
}