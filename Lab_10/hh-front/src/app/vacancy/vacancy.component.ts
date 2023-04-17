import {Component, OnInit} from '@angular/core';
import {VacancyService} from "../vacancy.service";
import {Company, Vacancy} from "../models";
import {ActivatedRoute} from "@angular/router";
import {CompanyService} from "../company.service";

@Component({
  selector: 'app-vacancy',
  templateUrl: './vacancy.component.html',
  styleUrls: ['./vacancy.component.css']
})
export class VacancyComponent implements OnInit{
  title = 'vacancies'

  compVacancies: Vacancy[] = [];
  allVacancies: Vacancy[] = [];

  constructor(private route: ActivatedRoute,
              private vacancyService: VacancyService,
              private companyService: CompanyService,
  ) {}

  ngOnInit(): void {
    this.getCompanyVacancies();
  }

  getCompanyVacancies() {
    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get("id"));
      this.companyService.getCompanyVacancies(id).subscribe(
        (vacancies) => {
          this.compVacancies = vacancies;
        }
      )
    })
  }
  getTopTenVacancies() {
    this.vacancyService.getTopTenVacancies().subscribe(
      (vacancies) => {
        this.allVacancies = vacancies;
      }
    )
  }
  getAllVacancies() {
    this.vacancyService.getVacancies().subscribe(
      (vacancies) => {
        this.allVacancies = vacancies;
      }
    )
  }

  deleteVacancy(id: number) {
    this.vacancyService.deleteVacancy(id).subscribe((data)=>  {
      this.allVacancies = this.allVacancies.filter((vacancy) => vacancy.id !== id);
      this.compVacancies = this.compVacancies.filter((vacancy) => vacancy.id !== id);
      }
    )
  }



}
