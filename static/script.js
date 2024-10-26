$(function () {
  let inputCount = 1;

  $("#add-input").click(function () {
    $("#dynamic-inputs").append(`
            <div>
                <label for="input_${inputCount}">#${inputCount}:</label>
                <input name="input_${inputCount}" style="margin-top:5px;" type="text">
            </div>
        `);
    inputCount++;
  });
});
