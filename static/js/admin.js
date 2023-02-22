$(document).ready(function () {
    document.getElementById('label-head').textContent=" ";
    // $('.myTable').DataTable();

     $('.item').click(function() {
    var value = $(this).data('value');
    var selected=document.querySelectorAll('ul li')
         selected.forEach(function (item){
             return item.classList.remove('active');
         });
         $('.item[data-value="' + value + '"]').addClass('active');
  });

var len= $('.myTable').rows;
console.log(len);
    $('.myTable').DataTable({
        "searching": true,
        "sorting": [[0, 'asc']]

    });
    // let regparts = window.location.pathname.split('/')
    // let regdef = regparts[regparts.length - 1];
    //
    // document.getElementById("regionIndi").textContent = regdef;
    // document.getElementById("regiondrop").textContent=regdef;

    $("#subnet_logo").hover(function () {
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
    setInterval(function () {
        $.ajax({
            url: "/get_latest_ts",
            type: 'GET',
            success: function (res) {
                let prev_ts = $('#timestamp').text().replace('Timestamp: ', '').trim();
                if (prev_ts !== res) {
                    location.reload();
                }
            }
        });
    }, 3 * 60 * 1000);

});

function openSettings() {

    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl");
    const igw = document.getElementById("igw");
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

function openAdmin() {
    document.getElementById("access-cred").style.display = "none";
    location.reload();
}

function closeNav() {

    document.getElementById("sidebar").style.width = "90px";
    document.getElementById("nav-bar").style.width = "calc(100% - 70px)";
    document.getElementById("nav-bar").style.left = "70px";
    document.getElementById("timestamp").style.marginLeft = "140px";
    document.getElementById("cont_div").style.width = "calc(100% - 80px)";
    document.getElementById("cont_div").style.marginLeft = "90px";
    document.getElementById("opened-menu").style.display = "none";
    document.getElementById("subnets_text").style.display = "none";
    document.getElementById("vpc_text").style.display = "none";
    document.getElementById("load_text").style.display = "none";
    document.getElementById("nacl_text").style.display = "none";
    document.getElementById("igw_text").style.display = "none";
    document.getElementById("sqs_text").style.display = "none";
    document.getElementById("nat_text").style.display = "none";
    document.getElementById("tgw_text").style.display = "none";
    document.getElementById("rds_text").style.display = "none";
    document.getElementById("ats_text").style.display = "none";
    document.getElementById("vms_text").style.display = "none";
    document.getElementById("dynamo_text").style.display = "none";
    document.getElementById("sns_details").style.display = "none";


}

function openNav() {

    document.getElementById("sidebar").style.width = "260px";
    document.getElementById("nav-bar").style.width = "calc(100% - 240px)";
    document.getElementById("nav-bar").style.left = "240px";
    document.getElementById("timestamp").style.marginLeft = "80px";
    document.getElementById("opened-menu").style.display = "";
    document.getElementById("subnets_text").style.display = "";
    document.getElementById("cont_div").style.marginLeft = "280px";
    document.getElementById("vpc_text").style.display = "";
    document.getElementById("load_text").style.display = "";
    document.getElementById("nacl_text").style.display = "";
    document.getElementById("igw_text").style.display = "";
    document.getElementById("sqs_text").style.display = "";
    document.getElementById("nat_text").style.display = "";
    document.getElementById("tgw_text").style.display = "";
    document.getElementById("rds_text").style.display = "";
    document.getElementById("ats_text").style.display = "";
    document.getElementById("vms_text").style.display = "";
    document.getElementById("dynamo_text").style.display = "";
    document.getElementById("sns_details").style.display = "";

}


function subnets() {
    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl");
    const igw = document.getElementById("igw");
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
}

function vpcDetails() {

    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl");
    const igw = document.getElementById("igw");
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
}

function loadBalancer() {

    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl");
    const igw = document.getElementById("igw");
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
}

function nacl() {

    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl");
    const igw = document.getElementById("igw");
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
}

function igw() {

    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl");
    const igw = document.getElementById("igw");
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
}

function sqs() {

    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl");
    const igw = document.getElementById("igw");
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
    sns.style.display="none"
}

function nat() {

    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl");
    const igw = document.getElementById("igw");
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
}

function tgw() {

    const sns = document.getElementById("sns_details");
    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl");
    const igw = document.getElementById("igw");
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
}

function rds() {

    const sns = document.getElementById("sns_details");
    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl");
    const igw = document.getElementById("igw");
    const sqs = document.getElementById("sqs_details");
    const nat = document.getElementById("nat_details");
    const tgw = document.getElementById("tgw_details");
    const rds = document.getElementById("rds_details");
    const dynamo_db = document.getElementById("dynamo_db");
    const ts = document.getElementById("ts_details");
    const ec2 = document.getElementById("ec2_details");

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
}

function dynamo() {

    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl");
    const igw = document.getElementById("igw");
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
}

function ats() {

    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl");
    const igw = document.getElementById("igw");
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
}

function vms() {

    const sns = document.getElementById("sns_details");
    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl");
    const igw = document.getElementById("igw");
    const sqs = document.getElementById("sqs_details");
    const nat = document.getElementById("nat_details");
    const tgw = document.getElementById("tgw_details");
    const rds = document.getElementById("rds_details");
    const dynamo_db = document.getElementById("dynamo_db");
    const ts = document.getElementById("ts_details");
    const ec2 = document.getElementById("ec2_details");

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
}

function sns() {
    document.getElementById('label-head').textContent="SNS";

    const sns = document.getElementById("sns_details");
    const subnet_details = document.getElementById("subnet_details");
    const vpc = document.getElementById("vpc_details");
    const load_balancer = document.getElementById("load_balancer");
    const nacl = document.getElementById("nacl");
    const igw = document.getElementById("igw");
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
}

