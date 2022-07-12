let emailULList = document.getElementById('emailULList');
let LI = document.getElementsByTagName('li');


fetch("outlookexport.json")
.then(response => response.json())
.then(data => {

    
   
    const subject = data['Subject'];
    const date = document.getElementById('Date');
    const from = data['From: (Name)'];
    const fromAddress = data['From: (Address)'];
    const cc = data['CC: (Name)']
    const email = data['Body'];
   
 
    

    const newLI = document.createElement('LI');
    
    for (let i=0; i < 30; i++ ) {
      // 

      
       const emailBody = String(data[i]['Body']);
       const regex = /(#[0-9]+(-G[A-Z])*)/;
       const match = regex.exec(emailBody);
      
      
       if (match) {
         claimNum = match[0];
         console.log(claimNum);
       } else {
         console.log('no match');
       }

       const splitBody = emailBody.split('\n');
       joinBody = splitBody.join('\n');
       console.log(joinBody);
      
       emailContents = `<li><a href=""><div id="emailUL"><h2 id="claimNum">${claimNum}</h2><h3 id="Subject">${data[i]['Subject']}</h3>
       <h4 id="From">From: ${data[i]['From: (Name)']}:  ${data[i]['From: (Address)']}</h4><pre>Message: ${joinBody}</pre></div></a></li><hr/>
    //    
    `;

       newLI.innerHTML += emailContents;
       emailULList.appendChild(newLI);

        //             // Initialize new SpeechSynthesisUtterance object
        // let speech = new SpeechSynthesisUtterance();

        // // Set Speech Language
        // speech.lang = "en";

        // let voices = []; // global array of available voices

        // window.speechSynthesis.onvoiceschanged = () => {
        // // Get List of Voices
        // voices = window.speechSynthesis.getVoices();

        // // Initially set the First Voice in the Array.
        // speech.voice = voices[1];

        // // Set the Voice Select List. (Set the Index as the value, which we'll use later when the user updates the Voice using the Select Menu.)
        // // let voiceSelect = document.querySelector("#voices");
        // // voices.forEach((voice, i) => (voiceSelect.options[i] = new Option(voice.name, i)));
        // };

        // document.querySelector("#rate").addEventListener("input", () => {
        // // Get rate Value from the input
        // // const rate = document.querySelector("#rate").value;
        // const rate = 1.2;

        // // Set rate property of the SpeechSynthesisUtterance instance
        // speech.rate = rate;

        // // Update the rate label
        // document.querySelector("#rate-label").innerHTML = rate;
        // });

        // document.querySelector("#volume").addEventListener("input", () => {
        // // Get volume Value from the input
        // const volume = document.querySelector("#volume").value;

        // // Set volume property of the SpeechSynthesisUtterance instance
        // speech.volume = volume;

        // // Update the volume label
        // document.querySelector("#volume-label").innerHTML = volume;
        // });

        // document.querySelector("#pitch").addEventListener("input", () => {
        // // Get pitch Value from the input
        // const pitch = document.querySelector("#pitch").value;

        // // Set pitch property of the SpeechSynthesisUtterance instance
        // speech.pitch = pitch;

        // // Update the pitch label
        // document.querySelector("#pitch-label").innerHTML = pitch;
        // });

        // document.querySelector("#voices").addEventListener("change", () => {
        // // On Voice change, use the value of the select menu (which is the index of the voice in the global voice array)
        // speech.voice = voices[document.querySelector("#voices").value];
        // });

        // document.querySelector("#start").addEventListener("click", () => {
        // // Set the text property with the value of the textarea
        // //   speech.text = document.querySelector("textarea").value;
        // speech.text = data;

        // // Start Speaking
        // window.speechSynthesis.speak(speech);
        // });

        // document.querySelector("#pause").addEventListener("click", () => {
        // // Pause the speechSynthesis instance
        // window.speechSynthesis.pause();
        // });

        // document.querySelector("#resume").addEventListener("click", () => {
        // // Resume the paused speechSynthesis instance
        // window.speechSynthesis.resume();
        // });

        // document.querySelector("#cancel").addEventListener("click", () => {
        // // Cancel the speechSynthesis instance
        // window.speechSynthesis.cancel();
        // });

    }

        console.log(data);
})