void beautify(TH2F*&);
void draw(TH2F*);
void overlay(TProfile*, TProfile*, string*); 

void beautifier(const char* filename) {

  // Open file with histograms
  TFile* file = TFile::Open(filename);

  // Get histograms
  TH2F* hist = (TH2F*)file->Get("QIE_HEM3_Even_Phi");
  beautify(hist);
  hist->RebinY(4);
  hist->SetFillColor(kBlue);
  hist->GetXaxis()->SetRangeUser(285.5,405.5);
  //hist->GetXaxis()->SetNdivisions(350);
  gStyle->SetOptStat(0);
  //gStyle->SetStatY(.881);
  draw(hist);

  // Rinse and repeat with other histograms
  TH2F* hist2 = (TH2F*)file->Get("QIE_HEM3_Odd_Phi");
  beautify(hist2);
  hist2->RebinY(4);
  hist2->SetFillColor(kBlue);
  hist2->GetXaxis()->SetRangeUser(285.5,405.5);
  //hist2->GetXaxis()->SetNdivisions(350);
  gStyle->SetOptStat(0);;
  //gStyle->SetStatY(.9);
  draw(hist2);


  /*
  TH2F* hist3 = (TH2F*)file->Get("QIE_HEM3_vs_Even_Phi");
  beautify(hist3);
  hist3->RebinY(4);
  hist3->SetFillColor(kBlue);
  hist3->GetXaxis()->SetRangeUser(7.5,11.5);
  hist3->GetXaxis()->SetNdivisions(4);
  gStyle->SetOptStat(0);;
  //gStyle->SetStatY(.881);
  draw(hist3);

  TH2F* hist4 = (TH2F*)file->Get("QIE_HEM3_vs_Odd_Phi");
  beautify(hist4);
  hist4->RebinY(4);
  hist4->SetFillColor(kBlue);
  hist4->GetXaxis()->SetRangeUser(6.5,10.5);
  hist4->GetXaxis()->SetNdivisions(4);
  gStyle->SetOptStat(0);;
  //gStyle->SetStatY(.881);
  draw(hist4);
  */

//Code for HEM4 Plots:
  TH2F* hist3 = (TH2F*)file->Get("QIE_HEM4_Even_Phi");
  beautify(hist3);
  hist->RebinY(4);
  hist->SetFillColor(kBlue);
  hist->GetXaxis()->SetRangeUser(0.5,350.5);
  //hist->GetXaxis()->SetNdivisions(2000);
  //hist->GetXaxis()->SetTickLength(1);
  gStyle->SetOptStat(0);
  //gStyle->SetStatY(.881);
  draw(hist3);

  // Rinse and repeat with other histograms
  TH2F* hist4 = (TH2F*)file->Get("QIE_HEM4_Odd_Phi");
  beautify(hist4);
  hist2->RebinY(4);
  hist2->SetFillColor(kBlue);
  hist2->GetXaxis()->SetRangeUser(0.5,350.5);
  //hist2->GetXaxis()->SetNdivisions(350);
  //hist->GetXaxis()->SetTickLength(1);
  gStyle->SetOptStat(0);
  //gStyle->SetStatY(.9);
  draw(hist4);

  /*
  TH2F* hist7 = (TH2F*)file->Get("QIE_HEM4_vs_Even_Phi");
  beautify(hist7);
  hist3->RebinY(4);
  hist3->SetFillColor(kBlue);
  hist3->GetXaxis()->SetRangeUser(11.0,15.0);
  //hist3->GetXaxis()->SetNdivisions(500);
  gStyle->SetOptStat(0);
  //gStyle->SetStatY(.881);
  draw(hist7);

  TH2F* hist8 = (TH2F*)file->Get("QIE_HEM4_vs_Odd_Phi");
  beautify(hist8);
  hist4->RebinY(4);
  hist4->SetFillColor(kBlue);
  hist4->GetXaxis()->SetRangeUser(10.0,14.0);
  hist4->GetXaxis()->SetNdivisions(4);
  gStyle->SetOptStat(0);
  //gStyle->SetStatY(.881);
  draw(hist8);
  */

  //Getting Profile Plots for Overlay 
  TProfile* prof1 = (TProfile*)file->Get("QIE_HEM3_Odd_Phi_Profile");
  TProfile* prof2 = (TProfile*)file->Get("QIE_HEM4_Odd_Phi_Profile");
  string ID = "Odd";
  //overlay(prof1, prof2, ID);
  TCanvas* canv2 = new TCanvas("P", "", 1100, 800);
  canv2->Draw();
  prof1->SetMarkerStyle(20);
  prof1->SetMarkerColor(4);
  prof1->Draw("");
  prof2->Draw("same");
  prof2->SetMarkerStyle(32);
  prof2->SetMarkerColor(2);
  prof1->GetYaxis()->SetRangeUser(3125,3425);
  prof2->GetYaxis()->SetRangeUser(3125,3425);
  prof1->GetXaxis()->SetTitleOffset(1.0);
  prof1->GetYaxis()->SetTitleOffset(1.4);
  prof2->GetXaxis()->SetTitleOffset(1.0);
  prof2->GetYaxis()->SetTitleOffset(1.4);


  TLegend* leg = new TLegend(0.75, 0.78, 0.82, 0.88);
  leg->SetFillColor(kWhite);
  leg->SetLineColor(kWhite);
  leg->AddEntry(prof1, "HEM03");
  leg->AddEntry(prof2, "HEM04");
  leg->SetTextSize(0.04);
  leg->Draw();
  canv2->Update();
  canv2->Print(Form("HEM3_HEM4_Odd_Phi_Overlay.png"));
  canv2->Print(Form("HEM3_HEM4_Odd_Phi_Overlay.pdf"));
  canv2->Print(Form("HEM3_HEM4_Odd_Phi_Overlay.C"));

  TProfile* prof3 = (TProfile*)file->Get("QIE_HEM3_Even_Phi_Profile");
  TProfile* prof4 = (TProfile*)file->Get("QIE_HEM4_Even_Phi_Profile");
  string ID2 = "Even";
  //overlay(prof3, prof4, ID2);
  TCanvas* canv3 = new TCanvas("P", "", 1100, 800);
  canv3->Draw();
  prof3->SetMarkerStyle(20);
  prof3->SetMarkerColor(4);
  prof3->Draw("");
  prof4->SetMarkerStyle(32);
  prof4->SetMarkerColor(2);
  prof4->Draw("same");
  prof3->GetYaxis()->SetRangeUser(1500,1900);
  prof4->GetYaxis()->SetRangeUser(1500,1900);
  prof3->GetXaxis()->SetTitleOffset(1.0);
  prof3->GetYaxis()->SetTitleOffset(1.4);
  prof4->GetXaxis()->SetTitleOffset(1.0);
  prof4->GetYaxis()->SetTitleOffset(1.4);

  TLegend* leg2 = new TLegend(0.75, 0.78, 0.82, 0.88);
  leg2->SetFillColor(kWhite);
  leg2->SetLineColor(kWhite);
  leg2->AddEntry(prof3, "HEM03");
  leg2->AddEntry(prof4, "HEM04");
  //leg2->SetTextSize(0.05); 
  leg2->SetTextSize(0.04);
  leg2->Draw();
  canv3->Update();
  canv3->Print(Form("HEM3_HEM4_Even_Phi_Overlay.png"));
  canv3->Print(Form("HEM3_HEM4_Even_Phi_Overlay.pdf"));
  canv3->Print(Form("HEM3_HEM4_Odd_Phi_Overlay.C"));


}

void beautify(TH2F*& hist) {

  hist->GetXaxis()->SetTitleOffset(1.0);
  hist->GetYaxis()->SetTitleOffset(1.8);
  //hist->GetXaxis()->CenterTitle();
  //hist->GetYaxis()->CenterTitle();
  hist->GetXaxis()->SetTitleFont(42);
  //gStyle->SetTitleFont(32);
  hist->GetYaxis()->SetTitleFont(42);
  hist->GetXaxis()->SetTitleSize(0.04);
  hist->GetYaxis()->SetTitleSize(0.04);

}

void draw(TH2F* hist) {

  TCanvas* canv = new TCanvas("c","",900,800);

  canv->Draw();

  hist->Draw("colz");

  canv->SetLeftMargin(0.15);
  canv->SetRightMargin(canv->GetLeftMargin());
    
  canv->Print(Form("%s.png",hist->GetName()));
  canv->Print(Form("%s.pdf",hist->GetName()));
  canv->Print(Form("%s.C",hist->GetName()));

}

//Try overlaying in C++ Beautify File???  Create additional beautify and draw functions 
 
/*void overlay(TProfile* prof, TProfile* prof2, string* ID) {

   TCanvas* canv2 = new TCanvas("P", "", 600,400);
   canv2->Draw();
   prof1->Draw();
   prof2->Draw("same");
   canv2->Update();
   canv2->Print(Form("HEM3_HEM4_%s_Phi_Overlay.png", ID));
   canv2->Print(Form("HEM3_HEM4_%s_Phi_Overlay.pdf", ID));
   canv2->Print(Form("HEM3_HEM4_%s_Phi_Overlay.C", ID));







}
*/
