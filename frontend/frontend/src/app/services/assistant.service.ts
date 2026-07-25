import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AssistantService {

  private apiUrl =
'http://127.0.0.1:8000/api/assistant/chat';



constructor(
private http:HttpClient
){}



askQuestion(question:string){

return this.http.post<any>(
this.apiUrl,
{
question
}
);

}
}
