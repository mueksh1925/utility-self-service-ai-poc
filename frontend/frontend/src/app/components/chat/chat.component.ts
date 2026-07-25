import { Component } from '@angular/core';
import { AssistantService } from '../../services/assistant.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-chat',
  imports: [CommonModule,FormsModule],
  templateUrl: './chat.component.html',
  styleUrl: './chat.component.scss'
})
export class ChatComponent {
question='';


messages:any[]=[];



constructor(
private assistant:
AssistantService,
private http:HttpClient
){}



sendMessage(){


this.messages.push({

sender:'Customer',

text:this.question

});


  this.http.post(
    'http://127.0.0.1:8000/api/assistant/chat',
    {
      question: this.question
    }
  )
  .subscribe({
    next: (response:any) => {
      console.log(response);
    },
    error: (error:any) => {
      console.error(error);
    }
  });
// this.assistant
// .askQuestion(this.question)
// .subscribe(response=>{
// console.log("Ehllo");

// this.messages.push({

// sender:'AI Assistant',

// text:
// response.answer

// });


// });


this.question='';


}

}
