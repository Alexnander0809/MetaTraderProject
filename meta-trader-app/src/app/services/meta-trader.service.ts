import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MetaTraderService {
  private apiUrl = 'https://tu-dominio/api/metatrader';

  constructor(private http: HttpClient) {}

  getAccountInfo(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/account-info`);
  }

  getNextMonthBalance(currentBalance: number, monthlyRate: number): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/next-month-balance`, {
      params: {
        currentBalance: currentBalance.toString(),
        monthlyRate: monthlyRate.toString()
      }
    });
  }
}
