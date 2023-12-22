import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class SendCodeService {

  constructor(private http: HttpClient) { }

  result: string = 'primero';
  sendCode(code: string) {
    return this.http.post('http://localhost:5000/api/code',  code )
  }
}
