import {Component, OnInit} from '@angular/core';
import {Company, Vacancy} from "../models";
import {CompanyService} from "../company.service";
import {ActivatedRoute} from "@angular/router";
import {VacancyService} from "../vacancy.service";

@Component({
  selector: 'app-company',
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.css']
})
export class CompanyComponent implements OnInit {

  newCompanyName: string = "";
  newCompanyDescr: string = "";
  newCompanyCity: string = "";
  newCompanyAddress: string = "";


  updCompanyName: string = "";
  updCompanyDescr: string = "";
  updCompanyCity: string = "";
  updCompanyAddress: string = "";
  companies: Company[] = [];
  choosenVacancies: Vacancy[] = [];

  constructor(private companyService: CompanyService,  private vacancyService: VacancyService,private route: ActivatedRoute) {}

  ngOnInit() : void {
    this.getCompanies();
  }

  getCompanies() {
    this.companyService.getCompanies().subscribe((companies) => {
      this.companies = companies;
    });
    return this.companies;
  }

  addCompany() {
    this.companyService.postCompany(
      this.newCompanyName,
      this.newCompanyDescr,
      this.newCompanyCity,
      this.newCompanyAddress
    ).subscribe((company) => {
        this.companies.push(company);
        this.newCompanyName = "";
        this.newCompanyDescr = "";
        this.newCompanyCity = "";
        this.newCompanyAddress = "";
      }
    )
  }

  deleteCompany(id: number) {
    this.companyService.deleteCompany(id).subscribe((data) => {
      this.companies = this.companies.filter((company) =>company.id !== id);
    })
  }

  updateCompany(id: number) {
    this.companyService.putCompany(
      id,
      this.updCompanyName,
      this.updCompanyDescr,
      this.updCompanyCity,
      this.updCompanyAddress
    ).subscribe((data) => {
      console.log("--DATA------->", data);

      this.getCompanies();
      this.updCompanyName = "";
      this.updCompanyDescr = "";
      this.updCompanyCity = "";
      this.updCompanyAddress = "";
    });
  }




}
