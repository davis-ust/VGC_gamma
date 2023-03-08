let clickedLinkText;
let cur_table = ""
var table
$(document).ready(function () {


    document.getElementById('label-head').textContent = "";

    //tables show function
    $('.ats').click(function () {
        // Convert table 2 to DataTable
        cur_table = $(this).data('table-selector');

        $(cur_table).each(function () {
            console.log(cur_table, "koi")
            table = $(this).DataTable();
            console.log(table, "table tab;ee")
            filter();
        });


        $('.filterTab').css("display", "none");
        $('.content_div').css("width", "calc(100% - 30px)");
        $('.filtericon').css("right", "170px");
        $('.dataTables_info').css("right", "20px");
        $('.dataTables_length').css("right", "20px");
        $('.dataTables_length').css("width", "calc(100% - 1151px)");
        document.getElementById('label-head').textContent = "Amazon Transfer Service";
        document.getElementById("mySidenav").style.width = "0";
        const subnet_details = document.getElementById("subnet_details");
        const vpc = document.getElementById("vpc_details");
        const load_balancer = document.getElementById("load_balancer");
        const nacl = document.getElementById("nacl_details");
        const igw = document.getElementById("igw_details");
        const sqs = document.getElementById("sqs_details");
        const nat = document.getElementById("nat_details");
        const tgw = document.getElementById("tgw_details");
        const rds = document.getElementById("rds_details");
        const dynamo_db = document.getElementById("dynamo_db");
        const ts = document.getElementById("ts_details");
        const ec2 = document.getElementById("ec2_details");
        const sns = document.getElementById("sns_details");
        const dash = document.getElementById("dash-view");

        dash.style.display = "none";
        sns.style.display = "none"
        subnet_details.style.display = "none";
        vpc.style.display = "none";
        load_balancer.style.display = "none";
        nacl.style.display = "none";
        igw.style.display = "none";
        sqs.style.display = "none";
        nat.style.display = "none";
        tgw.style.display = "none";
        rds.style.display = "none";
        dynamo_db.style.display = "none";
        ts.style.display = "flex";
        ec2.style.display = "none";


    });
    $('.subnets').click(function () {
        cur_table = $(this).data('table-selector');

        $(cur_table).each(function () {
            console.log(cur_table, "koi")
            table = $(this).DataTable();
            console.log(table, "table tab;ee")
            filter();
        });

        $('.filterTab').css("display", "none");
        $('.content_div').css("width", "calc(100% - 30px)");
        $('.filtericon').css("right", "170px");
        $('.dataTables_info').css("right", "20px");
        $('.dataTables_length').css("right", "20px");
        $('.dataTables_length').css("width", "calc(100% - 1151px)");
        document.getElementById('label-head').textContent = "SUBNETS";
        document.getElementById("mySidenav").style.width = "0";
        const subnet_details = document.getElementById("subnet_details");
        const vpc = document.getElementById("vpc_details");
        const load_balancer = document.getElementById("load_balancer");
        const nacl = document.getElementById("nacl_details");
        const igw = document.getElementById("igw_details");
        const sqs = document.getElementById("sqs_details");
        const nat = document.getElementById("nat_details");
        const tgw = document.getElementById("tgw_details");
        const rds = document.getElementById("rds_details");
        const dynamo_db = document.getElementById("dynamo_db");
        const ts = document.getElementById("ts_details");
        const ec2 = document.getElementById("ec2_details");
        const sns = document.getElementById("sns_details");
        const dash = document.getElementById("dash-view");

        dash.style.display = "none";
        sns.style.display = "none"
        subnet_details.style.display = "flex";
        vpc.style.display = "none";
        load_balancer.style.display = "none";
        nacl.style.display = "none";
        igw.style.display = "none";
        sqs.style.display = "none";
        nat.style.display = "none";
        tgw.style.display = "none";
        rds.style.display = "none";
        dynamo_db.style.display = "none";
        ts.style.display = "none";
        ec2.style.display = "none";
    });
    $('.vpc').click(function () {
        cur_table = $(this).data('table-selector');
        $(cur_table).each(function () {
            table = $(this).DataTable();
            filter();
        });

        $('.filterTab').css("display", "none");
        $('.content_div').css("width", "calc(100% - 30px)");
        $('.filtericon').css("right", "170px");
        $('.dataTables_info').css("right", "20px");
        $('.dataTables_length').css("right", "20px");
        $('.dataTables_length').css("width", "calc(100% - 1151px)");
        document.getElementById('label-head').textContent = "VPC DETAILS";
        document.getElementById("mySidenav").style.width = "0";
        const subnet_details = document.getElementById("subnet_details");
        const vpc = document.getElementById("vpc_details");
        const load_balancer = document.getElementById("load_balancer");
        const nacl = document.getElementById("nacl_details");
        const igw = document.getElementById("igw_details");
        const sqs = document.getElementById("sqs_details");
        const nat = document.getElementById("nat_details");
        const tgw = document.getElementById("tgw_details");
        const rds = document.getElementById("rds_details");
        const dynamo_db = document.getElementById("dynamo_db");
        const ts = document.getElementById("ts_details");
        const ec2 = document.getElementById("ec2_details");
        const sns = document.getElementById("sns_details");
        const dash = document.getElementById("dash-view");

        dash.style.display = "none";
        sns.style.display = "none"
        subnet_details.style.display = "none";
        vpc.style.display = "flex";
        load_balancer.style.display = "none";
        nacl.style.display = "none";
        igw.style.display = "none";
        sqs.style.display = "none";
        nat.style.display = "none";
        tgw.style.display = "none";
        rds.style.display = "none";
        dynamo_db.style.display = "none";
        ts.style.display = "none";
        ec2.style.display = "none";

    });
    $('.lb').click(function () {
        cur_table = $(this).data('table-selector');
        $(cur_table).each(function () {
            table = $(this).DataTable();
            filter();
        });

        $('.filterTab').css("display", "none");
        $('.content_div').css("width", "calc(100% - 30px)");
        $('.filtericon').css("right", "170px");
        $('.dataTables_info').css("right", "20px");
        $('.dataTables_length').css("right", "20px");
        $('.dataTables_length').css("width", "calc(100% - 1151px)");
        document.getElementById('label-head').textContent = "LOAD BALANCER";
        document.getElementById("mySidenav").style.width = "0";
        const subnet_details = document.getElementById("subnet_details");
        const vpc = document.getElementById("vpc_details");
        const load_balancer = document.getElementById("load_balancer");
        const nacl = document.getElementById("nacl_details");
        const igw = document.getElementById("igw_details");
        const sqs = document.getElementById("sqs_details");
        const nat = document.getElementById("nat_details");
        const tgw = document.getElementById("tgw_details");
        const rds = document.getElementById("rds_details");
        const dynamo_db = document.getElementById("dynamo_db");
        const ts = document.getElementById("ts_details");
        const ec2 = document.getElementById("ec2_details");
        const sns = document.getElementById("sns_details");
        const dash = document.getElementById("dash-view");

        dash.style.display = "none";
        sns.style.display = "none"
        subnet_details.style.display = "none";
        vpc.style.display = "none";
        load_balancer.style.display = "flex";
        nacl.style.display = "none";
        igw.style.display = "none";
        sqs.style.display = "none";
        nat.style.display = "none";
        tgw.style.display = "none";
        rds.style.display = "none";
        dynamo_db.style.display = "none";
        ts.style.display = "none";
        ec2.style.display = "none";
    });
    $('.nacl').click(function () {
        cur_table = $(this).data('table-selector');
        $(cur_table).each(function () {
            table = $(this).DataTable();
            filter();
        });
        $('.filterTab').css("display", "none");
        $('.content_div').css("width", "calc(100% - 30px)");
        $('.filtericon').css("right", "170px");
        $('.dataTables_info').css("right", "20px");
        $('.dataTables_length').css("right", "20px");
        $('.dataTables_length').css("width", "calc(100% - 1151px)");
        document.getElementById('label-head').textContent = "NACL";
        document.getElementById("mySidenav").style.width = "0";
        const subnet_details = document.getElementById("subnet_details");
        const vpc = document.getElementById("vpc_details");
        const load_balancer = document.getElementById("load_balancer");
        const nacl = document.getElementById("nacl_details");
        const igw = document.getElementById("igw_details");
        const sqs = document.getElementById("sqs_details");
        const nat = document.getElementById("nat_details");
        const tgw = document.getElementById("tgw_details");
        const rds = document.getElementById("rds_details");
        const dynamo_db = document.getElementById("dynamo_db");
        const ts = document.getElementById("ts_details");
        const ec2 = document.getElementById("ec2_details");
        const sns = document.getElementById("sns_details");
        const dash = document.getElementById("dash-view");

        dash.style.display = "none";
        sns.style.display = "none"
        subnet_details.style.display = "none";
        vpc.style.display = "none";
        load_balancer.style.display = "none";
        nacl.style.display = "flex";
        igw.style.display = "none";
        sqs.style.display = "none";
        nat.style.display = "none";
        tgw.style.display = "none";
        rds.style.display = "none";
        dynamo_db.style.display = "none";
        ts.style.display = "none";
        ec2.style.display = "none";
    });
    $('.igw').click(function () {
        cur_table = $(this).data('table-selector');
        $(cur_table).each(function () {
            table = $(this).DataTable();
            filter();
        });
        $('.filterTab').css("display", "none");
        $('.content_div').css("width", "calc(100% - 30px)");
        $('.filtericon').css("right", "170px");
        $('.dataTables_info').css("right", "20px");
        $('.dataTables_length').css("right", "20px");
        $('.dataTables_length').css("width", "calc(100% - 1151px)");
        document.getElementById('label-head').textContent = "IGW";
        document.getElementById("mySidenav").style.width = "0";
        const subnet_details = document.getElementById("subnet_details");
        const vpc = document.getElementById("vpc_details");
        const load_balancer = document.getElementById("load_balancer");
        const nacl = document.getElementById("nacl_details");
        const igw = document.getElementById("igw_details");
        const sqs = document.getElementById("sqs_details");
        const nat = document.getElementById("nat_details");
        const tgw = document.getElementById("tgw_details");
        const rds = document.getElementById("rds_details");
        const dynamo_db = document.getElementById("dynamo_db");
        const ts = document.getElementById("ts_details");
        const ec2 = document.getElementById("ec2_details");
        const sns = document.getElementById("sns_details");
        const dash = document.getElementById("dash-view");

        dash.style.display = "none";
        sns.style.display = "none"
        subnet_details.style.display = "none";
        vpc.style.display = "none";
        load_balancer.style.display = "none";
        nacl.style.display = "none";
        igw.style.display = "flex";
        sqs.style.display = "none";
        nat.style.display = "none";
        tgw.style.display = "none";
        rds.style.display = "none";
        dynamo_db.style.display = "none";
        ts.style.display = "none";
        ec2.style.display = "none";
    });
    $('.sqs').click(function () {
        cur_table = $(this).data('table-selector');
        $(cur_table).each(function () {
            table = $(this).DataTable();
            filter();
        });
        $('.filterTab').css("display", "none");
        $('.content_div').css("width", "calc(100% - 30px)");
        $('.filtericon').css("right", "170px");
        $('.dataTables_info').css("right", "20px");
        $('.dataTables_length').css("right", "20px");
        $('.dataTables_length').css("width", "calc(100% - 1151px)");
        document.getElementById('label-head').textContent = "SQS";
        document.getElementById("mySidenav").style.width = "0";
        const subnet_details = document.getElementById("subnet_details");
        const vpc = document.getElementById("vpc_details");
        const load_balancer = document.getElementById("load_balancer");
        const nacl = document.getElementById("nacl_details");
        const igw = document.getElementById("igw_details");
        const sqs = document.getElementById("sqs_details");
        const nat = document.getElementById("nat_details");
        const tgw = document.getElementById("tgw_details");
        const rds = document.getElementById("rds_details");
        const dynamo_db = document.getElementById("dynamo_db");
        const ts = document.getElementById("ts_details");
        const ec2 = document.getElementById("ec2_details");
        const sns = document.getElementById("sns_details");
        const dash = document.getElementById("dash-view");

        dash.style.display = "none";
        nacl.style.display = "none"
        subnet_details.style.display = "none";
        vpc.style.display = "none";
        load_balancer.style.display = "none";
        nacl.style.display = "none";
        igw.style.display = "none";
        sqs.style.display = "flex";
        nat.style.display = "none";
        tgw.style.display = "none";
        rds.style.display = "none";
        dynamo_db.style.display = "none";
        ts.style.display = "none";
        ec2.style.display = "none";
        sns.style.display = "none"
    });
    $('.nat').click(function () {
        cur_table = $(this).data('table-selector');
        $(cur_table).each(function () {
            table = $(this).DataTable();
            filter();
        });
        $('.filterTab').css("display", "none");
        $('.content_div').css("width", "calc(100% - 30px)");
        $('.filtericon').css("right", "170px");
        $('.dataTables_info').css("right", "20px");
        $('.dataTables_length').css("right", "20px");
        $('.dataTables_length').css("width", "calc(100% - 1151px)");
        document.getElementById('label-head').textContent = "NAT";
        document.getElementById("mySidenav").style.width = "0";
        const subnet_details = document.getElementById("subnet_details");
        const vpc = document.getElementById("vpc_details");
        const load_balancer = document.getElementById("load_balancer");
        const nacl = document.getElementById("nacl_details");
        const igw = document.getElementById("igw_details");
        const sqs = document.getElementById("sqs_details");
        const nat = document.getElementById("nat_details");
        const tgw = document.getElementById("tgw_details");
        const rds = document.getElementById("rds_details");
        const dynamo_db = document.getElementById("dynamo_db");
        const ts = document.getElementById("ts_details");
        const ec2 = document.getElementById("ec2_details");
        const sns = document.getElementById("sns_details");
        const dash = document.getElementById("dash-view");

        dash.style.display = "none";
        sns.style.display = "none"
        subnet_details.style.display = "none";
        vpc.style.display = "none";
        load_balancer.style.display = "none";
        nacl.style.display = "none";
        igw.style.display = "none";
        sqs.style.display = "none";
        nat.style.display = "flex";
        tgw.style.display = "none";
        rds.style.display = "none";
        dynamo_db.style.display = "none";
        ts.style.display = "none";
        ec2.style.display = "none";
    });
    $('.tgw').click(function () {
        cur_table = $(this).data('table-selector');
        $(cur_table).each(function () {
            table = $(this).DataTable();
            filter();
        });
        $('.filterTab').css("display", "none");
        $('.content_div').css("width", "calc(100% - 30px)");
        $('.filtericon').css("right", "170px");
        $('.dataTables_info').css("right", "20px");
        $('.dataTables_length').css("right", "20px");
        $('.dataTables_length').css("width", "calc(100% - 1151px)");
        document.getElementById('label-head').textContent = "TGW";
        document.getElementById("mySidenav").style.width = "0";
        const sns = document.getElementById("sns_details");
        const subnet_details = document.getElementById("subnet_details");
        const vpc = document.getElementById("vpc_details");
        const load_balancer = document.getElementById("load_balancer");
        const nacl = document.getElementById("nacl_details");
        const igw = document.getElementById("igw_details");
        const sqs = document.getElementById("sqs_details");
        const nat = document.getElementById("nat_details");
        const tgw = document.getElementById("tgw_details");
        const rds = document.getElementById("rds_details");
        const dynamo_db = document.getElementById("dynamo_db");
        const ts = document.getElementById("ts_details");
        const ec2 = document.getElementById("ec2_details");
        const dash = document.getElementById("dash-view");

        dash.style.display = "none";
        sns.style.display = "none"
        subnet_details.style.display = "none";
        vpc.style.display = "none";
        load_balancer.style.display = "none";
        nacl.style.display = "none";
        igw.style.display = "none";
        sqs.style.display = "none";
        nat.style.display = "none";
        tgw.style.display = "flex";
        rds.style.display = "none";
        dynamo_db.style.display = "none";
        ts.style.display = "none";
        ec2.style.display = "none";
    });
    $('.rds').click(function () {
        cur_table = $(this).data('table-selector');
        $(cur_table).each(function () {
            table = $(this).DataTable();
            filter();
        });
        $('.filterTab').css("display", "none");
        $('.content_div').css("width", "calc(100% - 30px)");
        $('.filtericon').css("right", "170px");
        $('.dataTables_info').css("right", "20px");
        $('.dataTables_length').css("right", "20px");
        $('.dataTables_length').css("width", "calc(100% - 1151px)");
        document.getElementById('label-head').textContent = "RDS";
        document.getElementById("mySidenav").style.width = "0";
        const sns = document.getElementById("sns_details");
        const subnet_details = document.getElementById("subnet_details");
        const vpc = document.getElementById("vpc_details");
        const load_balancer = document.getElementById("load_balancer");
        const nacl = document.getElementById("nacl_details");
        const igw = document.getElementById("igw_details");
        const sqs = document.getElementById("sqs_details");
        const nat = document.getElementById("nat_details");
        const tgw = document.getElementById("tgw_details");
        const rds = document.getElementById("rds_details");
        const dynamo_db = document.getElementById("dynamo_db");
        const ts = document.getElementById("ts_details");
        const ec2 = document.getElementById("ec2_details");
        const dash = document.getElementById("dash-view");

        dash.style.display = "none";
        subnet_details.style.display = "none";
        vpc.style.display = "none";
        load_balancer.style.display = "none";
        sns.style.display = "none";
        nacl.style.display = "none";
        igw.style.display = "none";
        sqs.style.display = "none";
        nat.style.display = "none";
        tgw.style.display = "none";
        rds.style.display = "flex";
        dynamo_db.style.display = "none";
        ts.style.display = "none";
        ec2.style.display = "none";
    });
    $('.dynamo').click(function () {
        cur_table = $(this).data('table-selector');
        $(cur_table).each(function () {
            table = $(this).DataTable();
            filter();
        });
        $('.filterTab').css("display", "none");
        $('.content_div').css("width", "calc(100% - 30px)");
        $('.filtericon').css("right", "170px");
        $('.dataTables_info').css("right", "20px");
        $('.dataTables_length').css("right", "20px");
        $('.dataTables_length').css("width", "calc(100% - 1151px)");
        document.getElementById('label-head').textContent = "DYNAMO DB";
        document.getElementById("mySidenav").style.width = "0";
        const subnet_details = document.getElementById("subnet_details");
        const vpc = document.getElementById("vpc_details");
        const load_balancer = document.getElementById("load_balancer");
        const nacl = document.getElementById("nacl_details");
        const igw = document.getElementById("igw_details");
        const sqs = document.getElementById("sqs_details");
        const nat = document.getElementById("nat_details");
        const tgw = document.getElementById("tgw_details");
        const rds = document.getElementById("rds_details");
        const dynamo_db = document.getElementById("dynamo_db");
        const ts = document.getElementById("ts_details");
        const ec2 = document.getElementById("ec2_details");
        const sns = document.getElementById("sns_details");
        const dash = document.getElementById("dash-view");

        dash.style.display = "none";
        sns.style.display = "none"
        subnet_details.style.display = "none";
        vpc.style.display = "none";
        load_balancer.style.display = "none";
        nacl.style.display = "none";
        igw.style.display = "none";
        sqs.style.display = "none";
        nat.style.display = "none";
        tgw.style.display = "none";
        rds.style.display = "none";
        dynamo_db.style.display = "flex";
        ts.style.display = "none";
        ec2.style.display = "none";
    });
    $('.sns').click(function () {
        cur_table = $(this).data('table-selector');
        $(cur_table).each(function () {
            table = $(this).DataTable();
            filter();
        });
        $('.filterTab').css("display", "none");
        $('.content_div').css("width", "calc(100% - 30px)");
        $('.filtericon').css("right", "170px");
        $('.dataTables_info').css("right", "20px");
        $('.dataTables_length').css("right", "20px");
        $('.dataTables_length').css("width", "calc(100% - 1151px)");
        document.getElementById('label-head').textContent = "SNS";
        document.getElementById("mySidenav").style.width = "0";
        const sns = document.getElementById("sns_details");
        const subnet_details = document.getElementById("subnet_details");
        const vpc = document.getElementById("vpc_details");
        const load_balancer = document.getElementById("load_balancer");
        const nacl = document.getElementById("nacl_details");
        const igw = document.getElementById("igw_details");
        const sqs = document.getElementById("sqs_details");
        const nat = document.getElementById("nat_details");
        const tgw = document.getElementById("tgw_details");
        const rds = document.getElementById("rds_details");
        const dynamo_db = document.getElementById("dynamo_db");
        const ts = document.getElementById("ts_details");
        const ec2 = document.getElementById("ec2_details");
        const dash = document.getElementById("dash-view");

        dash.style.display = "none";
        subnet_details.style.display = "none";
        vpc.style.display = "none";
        load_balancer.style.display = "none";
        nacl.style.display = "none";
        igw.style.display = "none";
        sqs.style.display = "none";
        nat.style.display = "none";
        tgw.style.display = "none";
        rds.style.display = "none";
        dynamo_db.style.display = "none";
        ts.style.display = "none";
        ec2.style.display = "none";
        sns.style.display = "flex";
    });
    $('.vms').click(function () {
        cur_table = $(this).data('table-selector');
        $(cur_table).each(function () {
            table = $(this).DataTable();
            filter();
        });
        $('.filterTab').css("display", "none");
        $('.content_div').css("width", "calc(100% - 30px)");
        $('.filtericon').css("right", "170px");
        $('.dataTables_info').css("right", "20px");
        $('.dataTables_length').css("right", "20px");
        $('.dataTables_length').css("width", "calc(100% - 1151px)");
        document.getElementById('label-head').textContent = "VMs";
        document.getElementById("mySidenav").style.width = "0";
        const sns = document.getElementById("sns_details");
        const subnet_details = document.getElementById("subnet_details");
        const vpc = document.getElementById("vpc_details");
        const load_balancer = document.getElementById("load_balancer");
        const nacl = document.getElementById("nacl_details");
        const igw = document.getElementById("igw_details");
        const sqs = document.getElementById("sqs_details");
        const nat = document.getElementById("nat_details");
        const tgw = document.getElementById("tgw_details");
        const rds = document.getElementById("rds_details");
        const dynamo_db = document.getElementById("dynamo_db");
        const ts = document.getElementById("ts_details");
        const ec2 = document.getElementById("ec2_details");
        const dash = document.getElementById("dash-view");

        dash.style.display = "none";
        subnet_details.style.display = "none";
        vpc.style.display = "none";
        load_balancer.style.display = "none";
        nacl.style.display = "none";
        igw.style.display = "none";
        sqs.style.display = "none";
        nat.style.display = "none";
        tgw.style.display = "none";
        rds.style.display = "none";
        dynamo_db.style.display = "none";
        ts.style.display = "none";
        ec2.style.display = "flex";
        sns.style.display = "none"
    });
    $('#closeButton').click(function () {
        $('.filterTab').css("display", "none");
        $('.content_div').css("width", "calc(100% - 30px)");
        $('.filtericon').css("right", "170px");
        $('.dataTables_info').css("right", "20px");
        $('.dataTables_length').css("right", "20px");
        $('.dataTables_length').css("width", "calc(100% - 1151px)");
    });
    $('#refLoad').click(function () {
        $('.loader').css("display", "flex");
        dropToggle();

    });
    $("#autoscan").click(function () {
        dropToggle();

    });
    $("#export").click(function () {
        dropToggle();
    });

    function dropToggle() {
        const divElement = document.querySelector('.dropdown-content');
        const classNames = divElement.className.substring(17);
        if (classNames === "show") {
            document.getElementById("dropdown-content").classList.toggle("show");
        }
    }

    //Filter Function
    function filter() {
        $(".filtericon").click(function () {
            $('.filterTab').css("display", "flex");
            $('.content_div').css("width", "calc(100% - 290px");
            $('.dataTables_info').css("right", "20px");
            $('.dataTables_length').css("right", "260px");
            $('.dataTables_length').css("width", "calc(100% - 1166px)");

            $('.filtericon').css("right", "395px");
        });

        var columnFilters = $('#columnFilters');
        columnFilters.empty();
        // Iterate over each column in the table
        table.columns().every(function (index) {

            // Get the header text for the current column
            var headerText = $(table.column(index).header()).text();

            // Create a new filter input for the current column
            var filterInput = $('<div>')
                .append($('<label style=" font-size: 12px;font-weight: 700;margin-right: 12px;">').text(headerText))
                .append($('<select style="height: 30px;outline: none;border: none;font-size: 12px;color: #ff8e3c;">').attr('data-column', index)
                    .append($('<option>').val('contains').text('Contains'))
                    .append($('<option>').val('equals').text('Equals'))
                    .append($('<option>').val('not_equals').text('Not Equals')))
                .append($('<input style="width: 180px;height: 18px;outline: none;">').attr('type', 'text'));

            // Add the new filter input to the container
            columnFilters.append(filterInput);
        });

        $('#filterButton').on('click', function () {

            table.columns().every(function (index) {

                // Get the filter settings for the current column
                var filterType = columnFilters.find('[data-column=' + index + ']').val();
                var searchTerm = columnFilters.find('[data-column=' + index + ']').next().val();

                console.log(filterType, "filtertype")
                console.log(searchTerm, "SearchTem")
                // Apply the selected filter for the current column
                switch (filterType) {
                    case 'contains':
                        table.column(index).search(searchTerm, true, false);
                        break;
                    case 'equals':
                        table.column(index).search('^' + searchTerm + '$', true, false);
                        break;
                    case 'not_equals':
                        table.column(index).search('^(?!' + searchTerm + '$).+', true, false);
                        break;
                }
            });

            // Redraw the table to apply the filters
            table.draw();
        });


        // Attach an event listener to the clear button
        $('#clearButton').on('click', function () {
            // Clear the filter for each column in the table
            table.columns().search('').draw();

            // Reset the filter inputs to their default values
            columnFilters.find('select').val('contains');
            columnFilters.find('input').val('');
        });
    }

    //Selected item highlight
    $('.item').click(function () {
        var value = $(this).data('value');
        var selected = document.querySelectorAll('ul li')
        selected.forEach(function (item) {
            return item.classList.remove('active');
        });
        $('.item[data-value="' + value + '"]').addClass('active');

    });


    $("#subnets").hover(function () {
        $(this).css('cursor', 'pointer').attr('title', 'Subnets');
    }, function () {
        $(this).css('cursor', 'auto');
    });
    $("#vpc_logo").hover(function () {
        $(this).css('cursor', 'pointer').attr('title', 'VPC');
    }, function () {
        $(this).css('cursor', 'auto');
    });
    $("#load_logo").hover(function () {
        $(this).css('cursor', 'pointer').attr('title', 'Load Balancer');
    }, function () {
        $(this).css('cursor', 'auto');
    });
    $("#nacl_logo").hover(function () {
        $(this).css('cursor', 'pointer').attr('title', 'NACL');
    }, function () {
        $(this).css('cursor', 'auto');
    });
    $("#igw_logo").hover(function () {
        $(this).css('cursor', 'pointer').attr('title', 'IGW');
    }, function () {
        $(this).css('cursor', 'auto');
    });
    $("#sqs_logo").hover(function () {
        $(this).css('cursor', 'pointer').attr('title', 'SQS');
    }, function () {
        $(this).css('cursor', 'auto');
    });
    $("#nat_logo").hover(function () {
        $(this).css('cursor', 'pointer').attr('title', 'NAT Gateway');
    }, function () {
        $(this).css('cursor', 'auto');
    });
    $("#tgw_logo").hover(function () {
        $(this).css('cursor', 'pointer').attr('title', 'TGW');
    }, function () {
        $(this).css('cursor', 'auto');
    });
    $("#rds_logo").hover(function () {
        $(this).css('cursor', 'pointer').attr('title', 'RDS');
    }, function () {
        $(this).css('cursor', 'auto');
    });
    $("#ats_logo").hover(function () {
        $(this).css('cursor', 'pointer').attr('title', 'Amazon Transfer Service');
    }, function () {
        $(this).css('cursor', 'auto');
    });
    $("#vms_logo").hover(function () {
        $(this).css('cursor', 'pointer').attr('title', 'VMs');
    }, function () {
        $(this).css('cursor', 'auto');
    });
    $("#refresh").hover(function () {
        $(this).css('cursor', 'pointer').attr('title', 'Get latest Results');
    }, function () {
        $(this).css('cursor', 'auto');
    });
    $("#export").hover(function () {
        $(this).css('cursor', 'pointer').attr('title', 'Export Data to Excel');
    }, function () {
        $(this).css('cursor', 'auto');
    });
    // setInterval(function () {
    //     $.ajax({
    //         url: "/get_latest_ts", type: 'GET', success: function (res) {
    //             let prev_ts = $('#timestamp').text().replace('Timestamp: ', '').trim();
    //             if (prev_ts !== res) {
    //                 location.reload();
    //             }
    //         }
    //     });
    // }, 3 * 60 * 1000);

});

function openConfirm() {
    var conDiv = document.getElementById('confirmPopup');
    conDiv.style.display = "block";
    $("table").on('click', '.delete_region', function () {
        var currentRow = $(this).closest("tr");
        console.log(currentRow)
        var del1 = currentRow.find(".regionKey").text().trim(); // get current row 1st TD value
        console.log(del1, 'hostname')
        var del2 = currentRow.find("td:eq(1)").text().split(' ',)[0];
        console.log(del2, 'interval')
        var del3 = currentRow.find("td:eq(1)").text().split(' ',)[1];
        // var del4= currentRow.find(".status");

        $('.region-delete').val(del1);
        // $('.status').val(del4)
        // console.log($('.ip-delete').val(del1))
        $('.delete-time').val(del2);
        $('.delete-time-interval').val(del3);
    });

}

$('#del-reg').click(function () {
    var conDiv = document.getElementById('confirmPopup');
    conDiv.style.display = "none";
});

function openSettings() {

    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl_details");
    const igw = document.getElementById("igw_details");
    const sqs = document.getElementById("sqs_details");
    const nat = document.getElementById("nat_details");
    const tgw = document.getElementById("tgw_details");
    const rds = document.getElementById("rds_details");
    const dynamo_db = document.getElementById("dynamo_db");
    const ts = document.getElementById("ts_details");
    const ec2 = document.getElementById("ec2_details");
    const ac = document.getElementById("access-cred");
    const sns = document.getElementById("sns_details");
    subnet_details.style.display = "none";
    sns.style.display = "none";
    vpc.style.display = "none";
    load_balancer.style.display = "none";
    nacl.style.display = "none";
    igw.style.display = "none";
    sqs.style.display = "none";
    nat.style.display = "none";
    tgw.style.display = "none";
    rds.style.display = "none";
    dynamo_db.style.display = "none";
    ts.style.display = "none";
    ec2.style.display = "none";
    ac.style.display = "";

}

function closePop() {
    $('.popup-container:target').style.visibility = 'hidden';
}

function openAdmin() {
    document.getElementById("access-cred").style.display = "none";
    location.reload();
}

function opendash() {
    document.getElementById('label-head').textContent = " ";

    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl_details");
    const igw = document.getElementById("igw_details");
    const sqs = document.getElementById("sqs_details");
    const nat = document.getElementById("nat_details");
    const tgw = document.getElementById("tgw_details");
    const rds = document.getElementById("rds_details");
    const dynamo_db = document.getElementById("dynamo_db");
    const ts = document.getElementById("ts_details");
    const ec2 = document.getElementById("ec2_details");
    const sns = document.getElementById("sns_details");
    const dash = document.getElementById("dash-view");

    dash.style.display = "flex";
    sns.style.display = "none"
    subnet_details.style.display = "none";
    vpc.style.display = "none";
    load_balancer.style.display = "none";
    nacl.style.display = "none";
    igw.style.display = "none";
    sqs.style.display = "none";
    nat.style.display = "none";
    tgw.style.display = "none";
    rds.style.display = "none";
    dynamo_db.style.display = "none";
    ts.style.display = "none";
    ec2.style.display = "none";
}

function getRegion(e) {
    document.getElementById("dropdown-content").classList.toggle("show")
    clickedLinkText = e.target.textContent;
    window.location.href = '/dashboard/' + clickedLinkText;
    $(".loader").css("display", "flex");
    document.getElementById("regionIndi").textContent = clickedLinkText;
    document.getElementById("regiondrop").textContent = clickedLinkText;
}

function openRegioDrop() {
    console.log(" clicked")
    document.getElementById("dropdown-content").classList.toggle("show");
}

