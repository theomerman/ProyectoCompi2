import { Component } from '@angular/core';
import { MonacoEditorModule } from 'ngx-monaco-editor-v2';
import { SendCodeService } from '../sendCode/send-code.service';
@Component({
  selector: 'app-output',
  standalone: true,
  imports: [],
  templateUrl: './output.component.html',
  styleUrl: './output.component.css'
})
export class OutputComponent {
  constructor(private result:SendCodeService){}
  response: string = this.result.result;
  
}
