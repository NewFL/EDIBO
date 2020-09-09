import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import {MatDividerModule} from '@angular/material/divider';
import {MatSliderModule} from '@angular/material/slider';
import {MatIconModule} from '@angular/material/icon';
import {MatListModule} from '@angular/material/list';

import { ButtonOverviewExample} from './button/button-overview-example';

@NgModule({
  declarations: [
    AppComponent,
    ButtonOverviewExample
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatDividerModule,
    MatSliderModule,
    MatIconModule,
    MatListModule
  ],
  providers: [],
  bootstrap: [AppComponent, ButtonOverviewExample]
})
export class AppModule { }
