$(document).ready(function () {

    $("#calculateButton").click(function () {
        var serializedData = $("#calculateTaxForm").serialize();

        $.ajax({
            url: 'api/calculate-tax/',
            data: JSON.stringify(serializedData),
            type: 'post',
            contentType: "application/json",
            success: function(response) {
                if(response.data.detail == true) {
                    $("#taxDetail").html('<div class="card mb-1"><div class="card-body"><ul class="list-group mb-3"><li class="list-group-item d-flex justify-content-between lh-sm"><div><h6 class="my-0">0% on earnings up to £12,500</h6></div><span class="text-muted">£0</span></li><li class="list-group-item d-flex justify-content-between lh-sm"><div><h6 class="my-0">20% on any earnings between £12,501 and £50,000</h6></div><span class="text-muted">£' + response.data.income_tax_slab_1 + '</span></li><li class="list-group-item d-flex justify-content-between lh-sm"><div><h6 class="my-0">40% on any earnings between £50,001 and £150,000</h6></div><span class="text-muted">£' + response.data.income_tax_slab_2 + '</span></li><li class="list-group-item d-flex justify-content-between lh-sm"><div><h6 class="my-0">45% on earnings of £150,001 and over</h6></div><span class="text-muted">£' + response.data.income_tax_slab_3 + '</span></li><li class="list-group-item d-flex justify-content-between"><span>Total tax (LBS)</span><strong>£' + response.data.tax_result + '</strong></li></ul>');
                } else {
                    $("#taxDetail").html('<div class="card mb-1"><div class="card-body"><ul class="list-group mb-3"><li class="list-group-item d-flex justify-content-between"><span>Total tax (LBS)</span><strong>£' + response.data.tax_result + '</strong></li></ul></div></div>');
                }
            },
            error: function (response, status, error) {

                $("#taxDetail").html('<div class="card mb-1"><div class="card-body">' + JSON.parse(response.responseText).data['income'] + '</div></div>');
            }
        })

        $("#calculateTaxForm")[0].reset();

    });

});
