function plus()
{
	let a = parseFloat(document.getElementById("num1").value);
	let b = parseFloat(document.getElementById("num2").value);
	let res;

	res = a + b;
	alert(res);
	console.log("Test JS")

	document.getElementById("result").innerText = " " + res;
}

function minus()
{
	let a = parseFloat(document.getElementById("num1").value);
	let b = parseFloat(document.getElementById("num2").value);
	let res;

	res = a - b;
	alert(res);
	console.log("Test JS")

	document.getElementById("result").innerText = " " + res;
}

function kob()
{
	let a = parseFloat(document.getElementById("num1").value);
	let b = parseFloat(document.getElementById("num2").value);
	let res;

	res = a * b;
	alert(res);
	console.log("Test JS")

	document.getElementById("result").innerText = " " + res;
}

function bol()
{
	let a = parseFloat(document.getElementById("num1").value);
	let b = parseFloat(document.getElementById("num2").value);
	let res;

	res = a / b;
	alert(res);
	console.log("Test JS")

	document.getElementById("result").innerText = " " + res;
}

function proverka()
{
	let a = parseFloat(document.getElementById("num1").value);
	let b = parseFloat(document.getElementById("num2").value);
	let res;

	if (a>b)
		res = ">";
	if (a<b)
		res = "<";
	if (a==b)
		res = "=";
	alert(res);
	console.log("Test JS")

	document.getElementById("result").innerText = " " + res;
}