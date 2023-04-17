import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {HttpClientModule} from "@angular/common/http";
import { VacancyComponent } from './vacancy/vacancy.component';
import {FormsModule} from "@angular/forms";
import { CompanyComponent } from './company/company.component';

@NgModule({
  declarations: [
    AppComponent,
    VacancyComponent,
    CompanyComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
