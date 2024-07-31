import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { AccountInfoComponent } from './components/account-info/account-info.component';
import { MetaTraderService } from './services/meta-trader.service';

@NgModule({
  declarations: [
    AppComponent,
    AccountInfoComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [MetaTraderService],
  bootstrap: [AppComponent]
})
export class AppModule { }
