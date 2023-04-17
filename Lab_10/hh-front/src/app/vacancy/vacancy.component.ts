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

  newVacName: string = "";
  newVacDescr: string = "";
  newVacSalary: number = 0;
  newVacCompany: Company | undefined;


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

  getAllVacancies() {
    this.vacancyService.getVacancies().subscribe(
      (vacancies) => {
        this.allVacancies = vacancies;
      }
    )
  }

  addVacancy() {

  }




}
