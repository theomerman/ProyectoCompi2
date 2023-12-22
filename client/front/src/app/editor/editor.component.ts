import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { SendCodeService } from '../sendCode/send-code.service';

@Component({
  selector: 'app-editor',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './editor.component.html',
  styleUrl: './editor.component.css'
})
export class EditorComponent {
  constructor(private sendCode:SendCodeService) { }
  query1: string = 'Hola mundo1';
  query2: string = 'Hola mundo2';
  query3: string = 'Hola mundo3';
  query4: string = 'Hola mundo4';
  
  sendData(){
    this.sendCode.sendCode(this.query1).subscribe(
      response => {
        console.log(this.sendCode.result)
        console.log('API Response:', response);
        this.sendCode.result = "response;";
        console.log(this.sendCode.result)
      },
      error => {
        console.error('API Error:', error);
      }
    );
  }
}
