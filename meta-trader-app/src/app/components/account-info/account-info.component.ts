import { Component, OnInit } from '@angular/core';
import { MetaTraderService } from '../../services/meta-trader.service';

@Component({
  selector: 'app-account-info',
  templateUrl: './account-info.component.html',
  styleUrls: ['./account-info.component.css']
})
export class AccountInfoComponent implements OnInit {
  accountInfo: any;
  nextMonthBalance: number | null = null;
  monthlyRate: number = 0;
  currentBalance: number = 0;

  constructor(private metaTraderService: MetaTraderService) {}

  ngOnInit(): void {
    this.metaTraderService.getAccountInfo().subscribe(data => {
      this.accountInfo = data;
      this.currentBalance = data.balance;
    });
  }

  calculateNextMonthBalance(): void {
    this.metaTraderService.getNextMonthBalance(this.currentBalance, this.monthlyRate).subscribe(data => {
      this.nextMonthBalance = data;
    });
  }
}
