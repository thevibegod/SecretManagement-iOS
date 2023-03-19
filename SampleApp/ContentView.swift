//
//  ContentView.swift
//  SampleApp
//
//  Created by Adarsh A on 18/03/23.
//

import SwiftUI

struct ContentView: View {

    private var apiKey1: String {
        SampleAppSecretManager.shared.apiKey1
    }

    private var apiKey2: String {
        SampleAppSecretManager.shared.apiKey2
    }

    var body: some View {
        VStack {
            Text("API KEY 1: \(apiKey1) \n\n API KEY 2: \(apiKey2)")
        }
        .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
