$(function () {
  let inputCount = 1;

  $("#add-input").click(function () {
    $("#dynamic-inputs").append(`
      <div class="input-group mb-3">
        <div class="input-group-prepend">
          <span class="input-group-text" id="inputGroup-sizing-default">#${inputCount}:</span>
        </div>
        <input
          name="input_${inputCount}"
          type="text"
          class="form-control"
          aria-label="Default"
          aria-describedby="inputGroup-sizing-default"
        />
      </div>
        `);
    inputCount++;
  });
});
