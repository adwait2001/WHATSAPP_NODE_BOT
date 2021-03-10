


function hello() {
  return "Hello, World!"
}

function switch0(arg0) {
  return switch1("Hi")
}

function switch1(argument) {
  console.log(argument)
  mydict = {
    "Hi": 'Hello',
    "1": "\n1: milk \n2: Dal\n3: Oil Products\n4: Soap\n'EXIT' to checkout\n'CART' to view cart",
    "2": "code       company       rate(inRs)\n 1            amul milk            56 \n 2            warna milk          56 \n  3            gokul milk           56 \n  4            nandini milk        54 \n\n\n1{ To continiue \n'BACK' to go back\n'EXIT' to checkout\n'CART' to view cart ",
    "3": "Code.        Company.          Rate \n 1.             Mug.                  80/kg\n 2.             Masoor.            60/kg\n 3.            Harbhara.          70/kg \n 4.             Toordal.            70/kg \n 5.             Masoordal.       75/kg \n\n\n1{ To continiue \n'BACK' to go back\n'EXIT' to checkout\n'CART' to view cart ",
    "4": "Code.         Company.       Price \n  1.               Fortune          130/kg \n 2.               Gemini.          128/kg \n 3.                Safola.          120/kg \n 4.               Star.                120/kg \n 5.                Kirtigold.       115/kg \n\n\n1{ To continiue \n'BACK' to go back\n'EXIT' to checkout\n'CART' to view cart ",
    "5": "code       company       rate(inRs) \n 1.         surfexcel soap         10 \n 2         vim soap                  10 \n 3         wheel soap               8 \n 4         tiptop soap               7 \n 5         hamam soap            6 \n\n\n1{ To continiue \n'BACK' to go back\n'EXIT' to checkout\n'CART' to view cart ",
    "Hi2.0": " to add next item in your cart,make your next choices \n1:milk \n2:dal\n3:oilProducts\n4:Soap ",
  }

  var a = "plz give correct input option number.I am still in learning phase."
  return (mydict[argument])
}

function switch2(arg3) {
  switcher = {
    "2": "how many litres of milk do you want?\n\n\n 'BACK' go back\n'EXIT' to checkout\n'CART' to view cart\n 'CAT' to view categories",
    "3": "how many grams or KGs of Dal you want to buy?\n\n\n 'BACK' go back\n'EXIT' to checkout\n'CART' to view cart\n 'CAT' to view categories",
    "4": "how many Kgs of oil do you need?\n 'BACK' go back\n\n\n'EXIT' to checkout\n'CART' to view cart\n 'CAT' to view categories",
    "5": "how many soaps do you want?\n\n\n 'BACK' go back\n'EXIT' to checkout\n'CART' to view cart\n 'CAT' to view categories",
  }
  return (switcher[arg3])
}
function switchq(argq) {
  switcherq = {
    "2": "litres",
    "3": "kg",
    "4": "kg",
    "5": "nos"
  }
  return (switcherq[argq])
}

function switch3(arg3) {
  var switchof = "select the correct option-- \n 1. add next  \n 2. no more ,place order"
  return (switchof)
}

function switch4(arg4) {
  dictl = {
    "1": switch1("Hi"),
    "2": "your order is taken by our side",
  }
  return (dict1[arg4])
}


var flag=0
var cat=0;
var final='Your Cart \nItem   Quantity\n'
var cart=[]

class sub1 {
  constructor(cust) {
    this.cust = cust;
  }


  add_and_show(arg) {
    if (['HI', 'hi', 'Hi'].includes(arg)) {
      return switch1("Hi")
    }
    else if (flag == 0 && arg == "1") {
      flag +=1
      console.log('here')
      return switch1("1")
    }
    else if (flag == 0 && arg == "2") {
      flag = 0
      return "Thankyou"
    }
    else if (arg == 'EXIT') {
      var op =final + 'Thank-you for shopping with us'
      return op
    }
    else if (arg == 'CAT') {
      flag = 1
      return switch1('1')
    }
    else if (arg == 'CART') {
      return final + "\n\n'EXIT' to checkout\n'CAT' to view categories"
    }
    else if (flag == 1 && (arg == "1" || arg == "2" || arg == "3" || arg == "4")) {
      console.log("here1")
      cat = (parseInt(arg) + 1).toString()
      flag += 1
      return switch1((parseInt(arg) + 1).toString())
    }
    else if (flag == 2 && arg == '1') {
      flag += 1
      return switch2(cat)
    }
    else if (flag == 3 && arg == 'BACK') {
      flag -= 1;
      return switch2(cat)
    }
    else if (flag == 3) {
      var lst = []
      var it ;
      var qu;
      lst = arg.split(" ")
     final += lst[0]
     final += "   "
     final += lst[1]
     final += ' '
     final += switchq(cat)
     final += '\n'
      op = "Succesfully Added to CART\n'EXIT' to checkout\n\n\n'CART' to view cart\n 'CAT' to view categories"
      // cart[cat][lst[0]] = lst[1]
      return op;
    }

    else if (flag == 3 && arg == 'BACK') {
      flag -= 1;
      return switch2(cat)
    }
    else if (flag == 2 && arg == 'BACK') {
      flag -= 1;
      return switch1("1")
    }
    else if (flag == 1 && arg == 'BACK') {
      flag -= 1;
      return ("Thankyou")
    }
    else {
      flag = 1
      console.log('here3')
      return switch1('1')
    }

  }
}