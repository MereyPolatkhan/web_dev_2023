import {Component, OnInit} from '@angular/core';
import {Vacancy} from "./models";
import {VacancyService} from "./vacancy.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'hh-front';

  vacancies: Vacancy[] = [];
  constructor(private vacancyService: VacancyService) {}

  ngOnInit() {
    this.vacancyService.getVacancies().subscribe((vacancies) => {
      this.vacancies = vacancies;
    });
  }



}
