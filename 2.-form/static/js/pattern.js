let types = {};
let VISA = "visa";
let MASTERCARD = "master-card";
let AMERICAN_EXPRESS = "american-express";
let DINERS_CLUB = "diners-club";
let DISCOVER = "discover";
let JCB = "jcb";
let UNIONPAY = "unionpay";
let MAESTRO = "maestro";
let CVV = "CVV";
let CID = "CID";
let CVC = "CVC";
let CVN = "CVN";
let testOrder = [
  VISA,
  MASTERCARD,
  AMERICAN_EXPRESS,
  DINERS_CLUB,
  DISCOVER,
  JCB,
  UNIONPAY,
  MAESTRO,
];

function clone(x) {
    // This a clone of a object of credict card
    // e.g. input x['visa'] 
    let prefixPattern, exactPattern, dupe;
    if (!x) {
        return null;
    }
    // extract the prefix pattern of the credict card
    prefixPattern = x.prefixPattern.source;
    // extract the exact pattern of the credict card
    exactPattern = x.exactPattern.source;
    // 
    dupe = JSON.parse(JSON.stringify(x));
    dupe.prefixPattern = prefixPattern;
    dupe.exactPattern = exactPattern;
    // output => the clone of this
    return dupe;
}

types[VISA] = {
  niceType: "Visa",
  className : "creditcard-icon--visa",
  type: VISA,
  prefixPattern: /^4$/,
  exactPattern: /^4\d*$/,
  gaps: [4, 8, 12],
  lengths: [16],
  code: {
    name: CVV,
    size: 3,
  },
};

types[MASTERCARD] = {
  niceType: "MasterCard",
  className:"creditcard-icon--master-card",
  type: MASTERCARD,
  prefixPattern: /^(5|5[1-5]|2|22|222|222[1-9]|2[3-6]|27[0-1]|2720)$/,
  exactPattern: /^(5[1-5]|222[1-9]|2[3-6]|27[0-1]|2720)\d*$/,
  gaps: [4, 8, 12],
  lengths: [16],
  code: {
    name: CVC,
    size: 3,
  },
};

types[AMERICAN_EXPRESS] = {
  niceType: "American Express",
  className:"creditcard-icon--master-card",
  type: AMERICAN_EXPRESS,
  prefixPattern: /^(3|34|37)$/,
  exactPattern: /^3[47]\d*$/,
  isAmex: true,
  gaps: [4, 10],
  lengths: [15],
  code: {
    name: CID,
    size: 4,
  },
};

types[DINERS_CLUB] = {
  niceType: "Diners Club",
  className:"creditcard-icon--american-express",
  type: DINERS_CLUB,
  prefixPattern: /^(3|3[0689]|30[0-5])$/,
  exactPattern: /^3(0[0-5]|[689])\d*$/,
  gaps: [4, 10],
  lengths: [14],
  code: {
    name: CVV,
    size: 3,
  },
};

types[DISCOVER] = {
  niceType: "Discover",
  className: "creditcard-icon--discover",
  type: DISCOVER,
  prefixPattern: /^(6|60|601|6011|65|64|64[4-9])$/,
  exactPattern: /^(6011|65|64[4-9])\d*$/,
  gaps: [4, 8, 12],
  lengths: [16, 19],
  code: {
    name: CID,
    size: 3,
  },
};

// types[JCB] = {
//   niceType: "JCB",
//   type: JCB,
//   prefixPattern: /^(2|21|213|2131|1|18|180|1800|3|35)$/,
//   exactPattern: /^(2131|1800|35)\d*$/,
//   gaps: [4, 8, 12],
//   lengths: [16],
//   code: {
//     name: CVV,
//     size: 3,
//   },
// };

// types[UNIONPAY] = {
//   niceType: "UnionPay",
//   type: UNIONPAY,
//   prefixPattern: /^(6|62)$/,
//   exactPattern: /^62\d*$/,
//   gaps: [4, 8, 12],
//   lengths: [16, 17, 18, 19],
//   code: {
//     name: CVN,
//     size: 3,
//   },
// };

// types[MAESTRO] = {
//   niceType: "Maestro",
//   type: MAESTRO,
//   prefixPattern: /^(5|5[06-9]|6\d*)$/,
//   exactPattern: /^5[06-9]\d*$/,
//   gaps: [4, 8, 12],
//   lengths: [12, 13, 14, 15, 16, 17, 18, 19],
//   code: {
//     name: CVC,
//     size: 3,
//   },
// };
// 
const typesValues=Object.values(types);

let cc_number = document.getElementById("cc_number");

let cc_input = document.getElementById("input--cc");

cc_number.addEventListener('input', (e) => {
    let target = e.target.value;

    if (target.length >=1) {
        
        typesValues.forEach( el => {
            const pattern  = RegExp(el.prefixPattern);
            if (target.match(pattern)) {                
                cc_input.className = el.className;
            }
        })
        
    }
    else {
        cc_input.className = ""
    }
    
        
});