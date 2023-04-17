import {Component, OnInit} from '@angular/core';
import {Company, Vacancy} from "./models";
import {VacancyService} from "./vacancy.service";
import {CompanyService} from "./company.service";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'hh-front';


}
